# -*- coding: utf-8 -*-
################################################################################
#
#    Odoo, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2017 Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

{
    'name': 'Record-keeping Attachment',
    'summary': 'Record-keeping Attachment for Odoo',
    'description': """
This module extends attachments with record-keeping fields
""",
    'version': '14.0.1',
    'category': 'Administration',
    'license': 'AGPL-3',
    'website': 'https://vertel.se',
    'author': 'Vertel AB',
    'depends': ['attachment_notebook', 'record_keeping', 'mail'],
    'data': [
        'views/ir_attachment_views.xml',
    ],
    'post_init_hook': 'post_init_hook',
}