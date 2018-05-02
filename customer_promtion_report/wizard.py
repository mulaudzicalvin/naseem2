#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class CustomerDetail(models.Model):
	_name = "customer.promt"

	date_from = fields.Date("Date From",required=True)
	date_to = fields.Date("Date To",required=True)
	supplier_id = fields.Many2many("res.partner",string="Customer")
	b_types = fields.Selection([('all','All'),('specfic', 'Specfic')], string="Filter", required=True)
	state = fields.Selection([('draft','Draft'),('confirm', 'Confirm'),('validate', 'Validate'),('cancel', 'Cancel')], string="State", required=True)









	
