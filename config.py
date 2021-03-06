# necessary import
import os
# Configs specific to this ervice
OBJECTS_API_TOKEN = 'this should be changed'
# URL to access the SIMBAB TAP interface
OBJECTS_SIMBAD_TAP_URL = 'http://simbad.u-strasbg.fr/simbad/sim-tap/sync'
# URL to access the NED interface
OBJECTS_NED_URL = 'http://ned.ipac.caltech.edu/srs/ObjectLookup'
# Time-out in seconds for SIMBAD TAP service requests
OBJECTS_SIMBAD_TIMEOUT = 4
# Time-out in seconds for NED service requests
OBJECTS_NED_TIMEOUT = 10
# Cache time-out in seconds (one day = 86400, one week = 604800)
OBJECTS_CACHE_TIMEOUT = 604800
# Default radius for cone search
OBJECTS_DEFAULT_RADIUS = 0.1
# Maximum number of records to return from cone search
OBJECTS_SIMBAD_MAX_REC = 10000
# Maximum number of records to send bibcodes back for
OBJECT_SOLR_MAX_HITS = 10000
# In what environment are we?
ENVIRONMENT = os.getenv('ENVIRONMENT', 'staging').lower()
# General config settings
API_URL = 'https://api.adsabs.harvard.edu'
# Where to send Solr queries
OBJECTS_SOLRQUERY_URL = '%s/v1/search/query' % API_URL
# Define caching type
CACHE_TYPE = 'simple'
# Define the autodiscovery endpoint
DISCOVERER_PUBLISH_ENDPOINT = '/resources'
# Advertise its own route within DISCOVERER_PUBLISH_ENDPOINT
DISCOVERER_SELF_PUBLISH = False
