# # -*- coding: utf-8 -*-
# # - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -
#
# __author__ = 'Satheesh R'
# A simple way to check the authentication using python ldap/ldaps
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import argparse

import ldap

# --------------------------------- Auth Config --------------------------------
# For normal use, change the below variable 'LDAP_SECURE' as False and for secure ldap use True for 'LDAP_SECURE'
LDAP_SECURE = True

AD_LDAP_SCHEME = 'ldaps' if LDAP_SECURE else 'ldap'
AD_LDAP_SERVER = "ldap.COMPANY.com"
AD_LDAP_PORT = 636 if LDAP_SECURE else 389
AD_LDAP_URL = f"{AD_LDAP_SCHEME}://{AD_LDAP_SERVER}:{AD_LDAP_PORT}"
AD_SEARCH_DN = "dc=company, dc=com"
AD_NT_DOMAIN = "COMPANY.com"
AD_SEARCH_FIELDS = ["mail", "displayName", "sn", "sAMAccountName", "memberOf"]


# --------------------------------- Auth Config --------------------------------


class LdapAuth:
    """
    class LdapAuth
    """

    def __init__(self, user_name, pass_word):
        """
        .
        """

        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

        self.con = ldap.initialize(AD_LDAP_URL)
        self.con.set_option(ldap.OPT_PROTOCOL_VERSION, 3)

        if LDAP_SECURE:
            self.con.set_option(ldap.OPT_REFERRALS, 0)
            self.con.set_option(ldap.OPT_X_TLS, ldap.OPT_X_TLS_DEMAND)
            self.con.set_option(ldap.OPT_X_TLS_DEMAND, True)
            self.con.set_option(ldap.OPT_DEBUG_LEVEL, 255)

        self.usr = user_name
        self.pwd = pass_word
        self.is_login = False

    def try_login(self):
        """

        :return:
        """

        ad_nt_domain = AD_NT_DOMAIN

        try:
            bind_dn = "%s@%s" % (self.usr.split('@')[0], AD_NT_DOMAIN)
            self.con.simple_bind_s(bind_dn, self.pwd)
            self.is_login = True
        except:
            pass

    def is_authenticated(self):
        """

        :return:
        """
        return self.is_login


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python LDAP/LDAP(S) login module', add_help=True)

    # Parser details
    parser.add_argument("-u", "--usr", default='', required=True, help='Username')
    parser.add_argument("-p", "--pwd", default='', required=True, help='Password')

    parser_args = vars(parser.parse_args())
    ladp_con = LdapAuth(parser_args['usr'], parser_args['pwd'])
    ladp_con.try_login()
    print(f'Successfully logged in.' if ladp_con.is_authenticated() else 'Failed ot login.')
