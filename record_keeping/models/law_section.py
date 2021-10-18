# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class LawSection(models.Model):
    """
    In order for a public authority to refuse to disclose information in an of-
    ficial document to a natural or legal person, or any kind of information
    to another public authority, in principle the information must be subject
    to secrecy. The public authority must examine whether there is any secrecy
    provision that may cover the information in question. If there is not, the
    information is public in all circumstances and must be disclosed.
    """
    _name = 'rk.law.section'
    _description = 'Record-keeping Law Section'
    _order = 'id desc'

    name = fields.Char()
    description = fields.Html()
    url = fields.Char()