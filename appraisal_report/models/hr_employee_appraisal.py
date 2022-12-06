# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError,Warning


class HrEmployeeAppraisal(models.Model):
    _inherit = 'hr.employee.appraisal'

    appraisal_percentage = fields.Char(compute='compute_appraisal_percentage')

    @api.onchange('total_deserve_appraisal', 'total_maximum_limit')
    def compute_appraisal_percentage(self):
        for record in self:
            if record.total_deserve_appraisal and record.total_maximum_limit:
                result = (record.total_deserve_appraisal / record.total_maximum_limit) * 100
                record.appraisal_percentage = str(result) + ' ' + '%'
            else:
                record.appraisal_percentage = ' '

    def get_report_error_message(self):
        print("::::::::::::::::::::::::ffffffffffffffffffffffffffffffffffffffffff")
        raise UserError(_("report must be completed and approved by manager"))
