# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
##############################################################################


{
    'name': 'my first module',
    'version': '1.0',
    'summary': 'Leads, Opportunities, Phone Calls',
    'description': """
The generic OpenERP Customer Relationship Management
====================================================

This application enables a group of people to intelligently and efficiently manage leads, opportunities, meetings and phone calls.

It manages key tasks such as communication, identification, prioritization, assignment, resolution and notification.

OpenERP ensures that all cases are successfully tracked by users, customers and suppliers. It can automatically send reminders, escalate the request, trigger specific methods and many other actions based on your own enterprise rules.

The greatest thing about this system is that users don't need to do anything special. The CRM module has an email gateway for the synchronization interface between mails and OpenERP. That way, users can just send emails to the request tracker.

OpenERP will take care of thanking them for their message, automatically routing it to the appropriate staff and make sure all future correspondence gets to the right place.


Dashboard for CRM will include:
-------------------------------
* Planned Revenue by Stage and User (graph)
* Opportunities by Stage (graph)
""",
    'author': 'OpenERP SA',
    'website': 'https://www.odoo.com/page/crm',
    'depends': ['base'],
    'data': [
        'openacademy_course_view.xml',
        'openacademy_session_view.xml'
        ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
