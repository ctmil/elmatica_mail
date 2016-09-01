from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)

class mail_followers(osv.Model):
	_inherit = 'mail.followers'

	def create(self, cr, uid, vals, context=None):
		if vals['res_model'] != 'crm.helpdesk':
        		res = super(mail_followers, self).create(cr, uid, vals, context=context)
		        self.invalidate_cache(cr, uid, context=context)
        		return res
		else:
			res = self.pool.get('mail.followers').search(cr,uid,[('res_model','=','crm.helpdesk'),\
				('res_id','=',vals['res_id'])])
			if res:
				if len(res) > 1:
					return res[0]
				else:
					return res
			else:
				return None


mail_followers()
