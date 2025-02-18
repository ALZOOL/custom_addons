import xmlrpc.client
from odoo import models, api
import logging
_logger = logging.getLogger(__name__)

class DataSync(models.Model):
    _name = 'data.sync'

    @api.model
    def sync_data(self):
        _logger.info("Starting data synchronization...")
        # إعداد الاتصال بقاعدة البيانات الأولى
        url_db1 = 'http://localhost:8095'
        db1 = 'testo_odoo'
        username_db1 = 'odoo5'
        password_db1 = 'md569ab27eb5ce96097de8610c8e48afdf1'

        # إعداد الاتصال بقاعدة البيانات الثانية
        url_db2 = 'http://localhost:8067'
        db2 = 'odoo'
        username_db2 = 'odoo'
        password_db2 = 'md5039b285724b3f3f29799d6d39a22fb2d'

        # إنشاء اتصال للقاعدة الأولى
        common_db1 = xmlrpc.client.ServerProxy(f'{url_db1}/xmlrpc/2/common')
        uid_db1 = common_db1.authenticate(db1, username_db1, password_db1, {})
        models_db1 = xmlrpc.client.ServerProxy(f'{url_db1}/xmlrpc/2/object')

        # إنشاء اتصال للقاعدة الثانية
        common_db2 = xmlrpc.client.ServerProxy(f'{url_db2}/xmlrpc/2/common')
        uid_db2 = common_db2.authenticate(db2, username_db2, password_db2, {})
        models_db2 = xmlrpc.client.ServerProxy(f'{url_db2}/xmlrpc/2/object')

        # جلب البيانات من قاعدة البيانات الأولى
        users_db1 = models_db1.execute_kw(db1, uid_db1, password_db1, 'res.users', 'search_read', [[]],{'fields': ['id', 'login']})
        # إدخال البيانات وربطها في قاعدة البيانات الثانية
        for user in users_db1:
            partner_id = models_db2.execute_kw(db2, uid_db2, password_db2, 'res.partner', 'create', [{
                'name': user['login'],
                'user_id': user['id'],
            }])
            _logger.info(f"Created partner with ID: {partner_id}")
            _logger.info("Data synchronization completed successfully.")
        else:
            _logger.error("Failed to authenticate with one or both databases.")

        #print("Data sync completed successfully.")
