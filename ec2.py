import base64
import json
import logging
import re


VALID_GROUP_PROGRESS = [
    'Launch',
    'Terminate',
    'HealthCheck',
    'ReplaceUnhealthy',
    'AZRebalance',
    'AlarmNotification',
    'ScheduledAction',
    'AddToLoadBalancer'
]



#if the values is not a list turn it into a list
#this function returns a dict of name and values
def fliter_kv(key, values):
    if not isinstance(values, list):
        values = [values]
    return {
        'Name': key,
        'Values': values
    }
    
def asg_tags(asg_name, ansible_artifact, ansible_extra_vars, ansible_tags, extra_tags=None):
    struct = {}
    if ansible_artifact:
        struct['a'] = ansible_artifact
    if ansible_extra_vars:
        struct['e'] = ansible_extra_vars
    if ansible_tags:
        struct['t'] = ansible_tags
        
    tags = {}
    if len(struct) > 0:
        tags['ansible'] = json.dumps(struct)
    tags['Name'] = asg_name
    tags['app'] = asg_name.split('-')[0]
    tags['stack'] = asg_name.split('-')[1]
    
    if extra_tags:
        for k, v in extra_tags.items():
            tags[k] = str(v)
    return tags
