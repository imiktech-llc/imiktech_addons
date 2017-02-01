# coding=utf-8
from odoo import api, models, _
from odoo.exceptions import AccessError


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def _attachment_force_storage(self):
        self.env['ir.attachment'].force_storage()

    @api.model
    def create(self, vals):
        res = super(IrConfigParameter, self).create(vals)
        if vals and vals.get('key') == 'ir_attachment.location':
            self._attachment_force_storage()
        return res

    @api.one
    def write(self, vals):
        res = super(IrConfigParameter, self).write(vals)
        if self.key == 'ir_attachment.location':
            self._attachment_force_storage()
        return res


class IrAttachmentWithForce(models.Model):
    _inherit = 'ir.attachment'

    def force_storage(self):
        if not self.env.user._is_admin():
            raise AccessError(_('Only administrators can execute this action.'))

        # domain to retrieve the attachments to migrate
        domain = {
            'db': [('store_fname', '!=', False)],
            'file': [('db_datas', '!=', False)],
        }[self._storage()]

        for attach in self.search(domain):
            attach.write({'datas': attach.datas, 'url': attach.url})
        return True
