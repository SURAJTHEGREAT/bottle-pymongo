from oslo_config import cfg
from oslo_config import types
import os
from logger.log import getLogger

# GENERATE THE LOG PATH FROM CURRENT FILE NAME
logpath = '/var/log/'+ os.path.splitext(os.path.basename(__file__))[0] + '.log'

LOG = getLogger(__name__,logpath)

PortType = types.Integer(1, 65535)


def do_register_opts(opts, group=None, ignore_errors=False):
    try:
        cfg.CONF.register_opts(opts, group=group)
    except:
        if not ignore_errors:
            raise


def do_register_cli_opts(opt, ignore_errors=False):
    # TODO: This function has broken name, it should work with lists :/
    if not isinstance(opt, (list, tuple)):
        opts = [opt]
    else:
        opts = opt

    try:
        cfg.CONF.register_cli_opts(opts)
    except:
        if not ignore_errors:
            raise

def register_opts(file_name):
    LOG.info("Into register method")
    LOG.info("The filename is")
    LOG.info(file_name)
    db_opts = [

    cfg.BoolOpt('db_enable',default=False),
    cfg.StrOpt('host', default='mongo', help='host of db server'),
    cfg.IntOpt('port', default=27017, help='port of db server'),
    cfg.StrOpt('db_name', default='', help='name of database'),
    cfg.StrOpt('username', help='username for db login'),
    cfg.StrOpt('password', default='', help='password for db login'),

    ]
    do_register_opts(db_opts, 'database')
    LOG.info("Register opts is complete")
# Common CLI options
    debug = cfg.BoolOpt('debug', default=False,
        help='Enable debug mode. By default this will set all log levels to DEBUG.')
    profile = cfg.BoolOpt('profile', default=False,
        help=('Enable profile mode. In the profile mode all the MongoDB queries and related '
'profile data are logged.'))

    cli_opts = [debug, profile]
    do_register_cli_opts(cli_opts)
    cfg.CONF(default_config_files=file_name)
    LOG.info("cfg.CONF is")
    LOG.info(cfg.CONF)
    return cfg.CONF

def conf_file(args=None):
    LOG.info("Into parse args method")
    try:
        pointer=register_opts(args)
    except Exception as e:
        LOG.info("The error is")
        LOG.info(e)
    LOG.info("The pointer is")
    LOG.info(pointer)
    return pointer



