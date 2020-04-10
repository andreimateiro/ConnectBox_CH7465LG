"""
Constants that define the functions of the modem
"""


class SetFunction:
    """
    Constants for the setters the modem in the modem's internal API
    """
    LANGUAGE = 4
    FACTORY_RESET = 7
    LOGIN = 15
    LOGOUT = 16
    CHANGE_PASSWORD = 18
    INSTALL_DONE = 20
    UPNP_STATUS = 101
    DHCP_V6 = 104
    DHCP_V4 = 106
    NAT_MODE = 108
    FILTER_RULE = 110
    IPV6_FILTER_RULE = 112
    FIREWALL = 116
    MACFILTER = 120
    PORT_FORWARDING = 122
    REBOOT = 133
    PING_TEST = 126
    TRACEROUTE = 127
    STOP_DIAGNOSTIC = 130
    REMOTE_ACCESS = 132
    MTU_SIZE = 135
    SET_EMAIL = 138
    SEND_EMAIL = 139
    PARENTAL_CONTROL = 141
    STATIC_DHCP_LEASE = 148
    WIFI_SETTINGS = 301


class GetFunction:
    """
    Constants for the getters in the modem's internal API
    """

    GLOBALSETTINGS = 1
    CM_SYSTEM_INFO = 2
    MULTILANG = 3
    STATUS = 5
    CONFIGURATION = 6
    DOWNSTREAM_TABLE = 10
    UPSTREAM_TABLE = 11
    SIGNAL_TABLE = 12
    EVENTLOG_TABLE = 13
    FIREWALLLOG_TABLE = 19
    LANGSETLIST = 21
    FAIL = 22
    LOGIN_TIMER = 24
    LANSETTING = 100
    DHCPV6INFO = 103
    BASICDHCP = 105
    WANSETTING = 107
    IPFILTERING = 109
    IPV6FILTERING = 111
    PORTTRIGGER = 113
    WEBFILTER = 115
    IPV6WEBFILTER = 117
    MACFILTERING = 119
    FORWARDING = 121
    LANUSERTABLE = 123
    DDNS = 124
    PING_RESULT = 128
    TRACEROUTE_RESULT = 129
    REMOTEACCESS = 131
    MTUSIZE = 134
    CMSTATE = 136
    WIREDSTATE = 137
    PARENTALCTL = 140
    WIREDSTATE_2 = 143
    CMSTATUS = 144
    ETHFLAPLIST = 147
    WIRELESSBASIC = 300
    WIRELESSWMM = 302
    WIRELESSSITESURVEY = 305
    WIRELESSGUESTNETWORK = 307
    CM_WIRELESSWPS = 309
    CM_WIRELESSACCESSCONTROL = 311
    CHANNELMAP = 313
    WIRELESSBASIC_2 = 315
    WIRELESSGUESTNETWORK_2 = 317
    WIRELESSCLIENT = 322
    CM_WIRELESSWPS_2 = 323
    DEFAULTVALUE = 324
    GSTRANDOMPASSWORD = 325
    WIFISTATE = 326
    WIRELESSRESETTING = 328
    STATUS_2 = 500
    QOSLIST = 502
    MTAEVENTLOGS = 503
    PROVIVSIONING = 504
