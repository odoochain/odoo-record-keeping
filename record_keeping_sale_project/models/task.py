# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def create_sale(self):
        self.ensure_one()
        if not self.partner_id:
            raise UserError('Please assign a customer to this task')
        else:
            self.create_matter()
            if not self.sale_order_id:
                self.sale_order_id = self.env['sale.order'].create(dict(
                    matter_id=self.matter_id.id,
                    is_official=True,
                    partner_id=self.partner_id.id,
                    project_id=False,
                ))
            
    def create_matter(self):
        self.ensure_one()
        if self.sale_order_id and self.sale_order_id.matter_id:
            self.matter_id = self.sale_order_id.matter_id
        else:
            super().create_matter()
            if self.sale_order_id and not self.sale_order_id.matter_id:
                self.sale_order_id.matter_id = self.matter_id
        
