from odoo import models, api, fields, _


class Slide(models.Model):
    _inherit = 'slide.slide'

    @api.multi
    def write(self, values):
        if values.get('datas') and not values.get('url'):
            values = {

            'image': self._fetch_data(google_values['thumbnailLink'].replace('=s220', ''), {}, 'image')['values'],
            'mime_type': google_values['mimeType'],
            'document_id': document_id,
        }doc_data = self._parse_document_url(values['url']).get('values', dict())
            for key, value in doc_data.iteritems():
                values.setdefault(key, value)
        if values.get('channel_id'):
            custom_channels = self.env['slide.channel'].search([('custom_slide_id', '=', self.id), ('id', '!=', values.get('channel_id'))])
            custom_channels.write({'custom_slide_id': False})
        res = super(Slide, self).write(values)
        if values.get('website_published'):
            self.date_published = datetime.datetime.now()
            self._post_publication()
        return res