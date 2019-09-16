# -*- coding: utf-8 -*-
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from odoo import _, models, fields, api
from odoo.modules import get_module_resource
from odoo.exceptions import ValidationError, UserError

class Medicalpatient(models.Model):
    _name = 'medical.patient'
    _description = 'Medical Patient'
    # _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(
        string='Name of patient',
        required=True,
    )
    function = fields.Char(
        string='Job title',
    )
    email = fields.Char()
    mobile = fields.Char()
    phone = fields.Char()

     # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized image of this contact. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this contact. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")
    age = fields.Char(
        compute='_compute_age',
    )
    active = fields.Boolean(
        default=True,
    )
    # partner_id = fields.Many2one(
    #     string='Related Partner',
    #     comodel_name='res.partner',
    #     required=True,
    #     ondelete='cascade',
    #     index=True,
    # )
    age_years = fields.Integer(
        string="Age (years old)",
        compute='_compute_age',
        search='_search_age',
    )
    identification_code = fields.Char(
        string='Internal Identification',
        help='Patient Identifier provided by the Health Center.'
             '(different from the Social Security Number)',
        default=lambda s: s.env['ir.sequence'].next_by_code(s._name ),
    )
    general_info = fields.Text(
        string='General Information',
    )
    is_deceased = fields.Boolean(
        compute='_compute_is_deceased',
    )
    marital_status = fields.Selection([
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ('z', 'law marriage'),
    ], )
    is_pregnant = fields.Boolean(
        help='Check this if the patient if pregnant',
    )
    date_death = fields.Datetime(
        string='Deceased Date',
    )

    # type = fields.Selection(
    #     default=lambda s: s._name,
    #     related='partner_id.type', )

    alias = fields.Char(
        string='Alias',
        help='Common name that the Party is referred',
    )

    count_patients = fields.Integer(
        compute='_compute_patient_ids_and_count',
    )
    birthdate_date = fields.Date(
        string='Birthdate',
    )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    weight = fields.Float()
    weight_uom = fields.Many2one(
        string="Weight UoM",
        comodel_name="product.uom",
        default=lambda s: s.env['res.lang'].default_uom_by_category('Weight'),
        domain=lambda self: [('category_id', '=',
                              self.env.ref('product.product_uom_categ_kgm').id)
                             ]
    )
   

    # @api.multi
    # def toggle_active(self):
    #     """ It toggles patient and partner activation. """
    #     for record in self:
    #         super(Medicalpatient, self).toggle_active()
    #         if record.active:
    #             record.partner_id.active = True
    #         else:
    #             entities = record.env[record._name].search([
    #                 ('partner_id', 'child_of', record.partner_id.id),
    #                 ('parent_id', 'child_of', record.partner_id.id),
    #                 ('active', '=', True),
    #             ])
    #             if not entities:
    #                 record.partner_id.active = False


    @api.multi
    def _compute_age(self):
        """ Age computed depending based on the birth date in the
         membership request.
        """
        now = datetime.now()
        for record in self:
            if record.birthdate_date:
                birthdate_date = fields.Datetime.from_string(
                    record.birthdate_date,
                )
                if record.is_deceased:
                    date_death = fields.Datetime.from_string(record.date_death)
                    delta = relativedelta(date_death, birthdate_date)
                    is_deceased = _(' (deceased)')
                else:
                    delta = relativedelta(now, birthdate_date)
                    is_deceased = ''
                years_months_days = '%d%s %d%s %d%s%s' % (
                    delta.years, _('y'), delta.months, _('m'),
                    delta.days, _('d'), is_deceased
                )
                years = delta.years
            else:
                years_months_days = _('No DoB')
                years = False
            record.age = years_months_days
            if years:
                record.age_years = years

    @api.multi
    def _compute_is_deceased(self):
        for record in self:
            record.is_deceased = bool(record.date_death)

    @api.multi
    @api.constrains('is_pregnant', 'gender')
    def _check_is_pregnant(self):
        for record in self:
            if record.is_pregnant and record.gender != 'female':
                raise ValidationError(_(
                    'Invalid selection - Only a `Female` may be pregnant.',
                ))

    @api.model
    def _create_vals(self, vals):
        vals = super(Medicalpatient, self).create(vals)
        if not vals.get('identification_code'):
            Seq = self.env['ir.sequence']
            vals['identification_code'] = Seq.sudo().next_by_code(
                self._name,
            )
        return vals

    @api.model_cr_context
    def _get_default_image_path(self, vals):
        super(Medicalpatient, self)._get_default_image_path(vals)
        return get_module_resource(
            'medical', 'static/src/img', 'patient-avatar.png',
        )

    def _search_age(self, operator, value):
        if operator not in ('ilike', '=', '>=', '>', '<', '<='):
            raise UserError(_('Invalid operator: %s' % (operator,)))

        current_date = date.today()
        last_birthdate = current_date + relativedelta(years=value * -1)
        first_birthdate = current_date + relativedelta(
            years=(value + 1) * -1,
            days=1,
        )
        last_possible_birthdate = fields.Datetime.to_string(last_birthdate)
        first_possible_birthdate = fields.Datetime.to_string(first_birthdate)

        if operator == '=' or operator == 'ilike':
            return ['&', ('birthdate_date', '>=', first_possible_birthdate),
                    ('birthdate_date', '<=', last_possible_birthdate)]
        elif operator == '>=':
            return [('birthdate_date', '<=', last_possible_birthdate)]
        elif operator == '>':
            return [('birthdate_date', '<', first_possible_birthdate)]
        elif operator == '<=':
            return [('birthdate_date', '>=', first_possible_birthdate)]
        elif operator == '<':
            return [('birthdate_date', '>', last_possible_birthdate)]

    def toggle_is_pregnant(self):
        self.toggle('is_pregnant')

    def toggle_safety_cap_yn(self):
        self.toggle('safety_cap_yn')

    def toggle_counseling_yn(self):
        self.toggle('counseling_yn')

    @api.multi
    def _get_medical_entity(self):
        self.ensure_one()
        if self.type and self.type[:7] == 'medical':
            return self.env[self.type].search([
                ('partner_id', '=', self.id),
            ])

    @api.multi
    def _compute_patient_ids_and_count(self):
        for record in self:
            patients = self.env['medical.patient'].search([
                ('partner_id', 'child_of', record.id),
            ])
            record.count_patients = len(patients)
            record.patient_ids = [(6, 0, patients.ids)]

    @api.multi
    @api.constrains('birthdate_date')
    def _check_birthdate_date(self):
        """ It will not allow birthdates in the future. """
        now = datetime.now()
        for record in self:
            if not record.birthdate_date:
                continue
            birthdate = fields.Datetime.from_string(record.birthdate_date)
            if birthdate > now:
                raise ValidationError(_(
                    'Partners cannot be born in the future.',
                ))
    
   

  
