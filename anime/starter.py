from django.shortcuts import render, redirect

from tools.elastic import ElasticSearchManager
from tools.dict import Dictionary


starter_dict = Dictionary()

####################################################################
########################## ElasticSearch ###########################
####################################################################
ES_NODE = 'http://127.0.0.1:9200'
starter_dict.add('es_manager', ElasticSearchManager.get_manager(ES_NODE))


####################################################################
############################ NOT FOUND #############################
####################################################################
def not_found_method():
    return redirect('/not-found/')

starter_dict.add('not_found_method', not_found_method)


####################################################################
############################ START FROM ############################
####################################################################
START_FROM_MAIN = 'watch'
START_FROM_CMS = 'anime'
starter_dict.add('main_start_from', START_FROM_MAIN)
starter_dict.add('cms_start_from', START_FROM_CMS)


def get_settings():
    return starter_dict.to_assosiative()
