from odoo import api, fields, models, tools, _

class PurchasePurchase(models.Model):
    _inherit = 'purchase.order.line'

    x_categ_id= fields.Many2one(related="product_id.categ_id", string=u'产品类别')

