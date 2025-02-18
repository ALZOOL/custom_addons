#python F:/odoo/Odoo-16.0/odoo-bin -c F:/debian/odoo2.conf --xmlrpc-port=8080
#python F:/odoo/Odoo-16.0/odoo-bin -c F:/debian/odoo2.conf --db_user=odoo3 --db_password=odoo --xmlrpc-port=8080
#python /server/odoo-bin -c /server/debian/odoo.conf
# import xmlrpc.client
#
# # إعداد المصادقة لقاعدة البيانات المصدر
# src_url = "http://source-odoo-server.com"
# src_db = "source-db"
# src_username = "source-user"
# src_password = "source-password"
#
# src_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(src_url))
# src_uid = src_common.authenticate(src_db, src_username, src_password, {})
# src_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(src_url))
#
# # إعداد المصادقة لقاعدة البيانات الهدف
# tgt_url = "http://target-odoo-server.com"
# tgt_db = "target-db"
# tgt_username = "target-user"
# tgt_password = "target-password"
#
# tgt_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(tgt_url))
# tgt_uid = tgt_common.authenticate(tgt_db, tgt_username, tgt_password, {})
# tgt_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(tgt_url))
#
# # استدعاء البيانات من قاعدة البيانات المصدر
# partners = src_models.execute_kw(src_db, src_uid, src_password, 'res.partner', 'search_read', [[]])
#
# # نقل البيانات إلى قاعدة البيانات الهدف
# for partner in partners:
#     tgt_models.execute_kw(tgt_db, tgt_uid, tgt_password, 'res.partner', 'create', [partner])
#
# ########################################################
# ########################################################
# #######################
# #######################
# #######################
# #source setting(src_url,src_db,src_username,src_password)
# #target setting(tgt_url, tgt_db, tgt_username, tgt_password)
# ################################################3
# ###################################################
# # import xmlrpc.client
# #
# # # إعداد المصادقة لقاعدة البيانات المصدر (odoo1.conf)
# # src_url = "http://localhost:8069"  # المنفذ المحدد في odoo1.conf
# # src_db = "odoo1_db"                # اسم قاعدة البيانات المستخدمة في odoo1.conf
# # src_username = "user1"             # اسم المستخدم المحدد في odoo1.conf
# # src_password = "password1"         # كلمة المرور المحددة في odoo1.conf
# #
# # src_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(src_url))
# # src_uid = src_common.authenticate(src_db, src_username, src_password, {})
# # src_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(src_url))
# #
# # # إعداد المصادقة لقاعدة البيانات الهدف (odoo2.conf)
# # tgt_url = "http://localhost:8079"  # المنفذ المحدد في odoo2.conf
# # tgt_db = "odoo2_db"                # اسم قاعدة البيانات المستخدمة في odoo2.conf
# # tgt_username = "user2"             # اسم المستخدم المحدد في odoo2.conf
# # tgt_password = "password2"         # كلمة المرور المحددة في odoo2.conf
# #
# # tgt_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(tgt_url))
# # tgt_uid = tgt_common.authenticate(tgt_db, tgt_username, tgt_password, {})
# # tgt_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(tgt_url))
# #
# # # استدعاء البيانات من قاعدة البيانات المصدر
# # partners = src_models.execute_kw(src_db, src_uid, src_password, 'res.partner', 'search_read', [[]])
# #
# # # نقل البيانات إلى قاعدة البيانات الهدف
# # for partner in partners:
# #     tgt_models.execute_kw(tgt_db, tgt_uid, tgt_password, 'res.partner', 'create', [partner])
# #####################################33333
# ####################################
# # مصدر قاعدة البيانات:
# #
# # src_url = "http://localhost:8069": عنوان خادم أودو المصدر مع المنفذ 8069 كما هو محدد في odoo1.conf.
# #
# # src_db = "odoo1_db": اسم قاعدة البيانات المستخدمة في odoo1.conf.
# #
# # src_username = "user1" و src_password = "password1": بيانات تسجيل الدخول المستخدمة في odoo1.conf.
# #
# # هدف قاعدة البيانات:
# #
# # tgt_url = "http://localhost:8079": عنوان خادم أودو الهدف مع المنفذ 8079 كما هو محدد في odoo2.conf.
# #
# # tgt_db = "odoo2_db": اسم قاعدة البيانات المستخدمة في odoo2.conf.
# #
# # tgt_username = "user2" و tgt_password = "password2": بيانات تسجيل الدخول المستخدمة في odoo2.conf.
# ##################################################
# ###################################################
# ################################################# odoo1.conf
# [options]
# addons_path = /opt/odoo/addons
# db_host = False
# db_port = False
# db_user = user1
# db_password = password1
# db_name = odoo1_db
# xmlrpc_port = 8069
# logfile = /var/log/odoo/odoo1.log
# ######################################################odoo2.conf
# [options]
# addons_path = /opt/odoo/addons
# db_host = False
# db_port = False
# db_user = user2
# db_password = password2
# db_name = odoo2_db
# xmlrpc_port = 8079
# logfile = /var/log/odoo/odoo2.log
# ########################################################
# /opt/odoo/odoo-bin -c /etc/odoo1.conf
# /opt/odoo/odoo-bin -c /etc/odoo2.conf
#./odoo-bin --config /debian/odoo2.conf
#./odoo-bin -r odoo -d odoo2
#./odoo-bin -r db_user -d db_name
#./odoo-bin --config /debian/odoo2.conf --without-demo=all --init=base

# ################################################3
# ##################################################
# ##################################################
# import xmlrpc.client
#
# # إعداد المصادقة لقاعدة البيانات المصدر (المستخدمين)
# src_url = "http://localhost:8069"
# src_db = "user_db"
# src_username = "user1"
# src_password = "password1"
#
# src_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(src_url))
# src_uid = src_common.authenticate(src_db, src_username, src_password, {})
# src_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(src_url))
#
# # إعداد المصادقة لقاعدة البيانات الهدف (المبيعات)
# tgt_url = "http://localhost:8079"
# tgt_db = "sales_db"
# tgt_username = "user2"
# tgt_password = "password2"
#
# tgt_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(tgt_url))
# tgt_uid = tgt_common.authenticate(tgt_db, tgt_username, tgt_password, {})
# tgt_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(tgt_url))
#
# # استدعاء بيانات المستخدمين من قاعدة البيانات المصدر
# def get_users():
#     return src_models.execute_kw(src_db, src_uid, src_password, 'res.users', 'search_read', [[]])
#
# # نقل بيانات المستخدمين إلى قاعدة البيانات الهدف
# def create_user_in_sales(user):
#     tgt_models.execute_kw(tgt_db, tgt_uid, tgt_password, 'res.users', 'create',
#################

###################

##################

#python odoo-bin -d testo_odoo -r odoo5 -w odoo --xmlrpc-port=8095 --addons-path=odoo/addons,odoo/custom_addons

#"C:\Program Files\PostgreSQL\12\bin\psql.exe" -U odoo5 -d odoo

#python odoo-bin -d odoo -r odoo -w odoo --xmlrpc-port=8067 --addons-path=addons,custom_addons

# for user in users_db1:
#     partner_id = models_db2.execute_kw(db2, uid_db2, password_db2, 'res.partner', 'create', [{
#         'name': user['login'],
#         'user_id': user['id'],
#     }])
#reset passwors UPDATE res_users SET password='odoo' WHERE login='admin';