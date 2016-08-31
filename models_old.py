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
		import pdb;pdb.set_trace()
        	res = super(mail_followers, self).create(cr, uid, vals, context=context)
	        self.invalidate_cache(cr, uid, context=context)
        	return res


mail_followers()
