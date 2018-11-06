#!/usr/bin/python


import iptc

import copy


EXPLODE_FIELDS = ["protocol"]


class InsertException(Exception):
    pass


class Rule(object):
    pass


class ConfigDict:
    def __init__(self, rule_obj):
        self.data = {}
        self.data.update(rule_obj)
        for key, value in self.data.iteritems():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        self.data[key] = value

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]
        else:
            raise AttributeError(item + " not defined")

    def __getattribute__(self, item):
        if item in self.data:
            return self.data[item]
        else:
            raise AttributeError(item + "not defined")

    def __len__(self):
        return self.data.__len__()

    def keys(self):
        return self.data.keys()

    def get(self, key, failobj=None):
        if key in self.data:
            return self.data[key]
        else:
            return failobj


def _generate_rule(rule_obj):
    rules = []

    for rule in rule_obj:
        tmp_rule = iptc.Rule()
        for key in rule.keys():
            if key != "match" and key != "target":
                setattr(tmp_rule, key, rule.get(key))

        target_str = rule.get("target")
        if target_str:
            target = iptc.Target(tmp_rule, rule.get("target"))
            tmp_rule.target = target
        rules.append(tmp_rule)

    return rules

"""
inserts a rule in the INPUT chain of iptables
takes one parameter which is a dictionary containing fields like src, protocol, target

"""


def insert_input(rule_obj):

    rules = []
    rule = ConfigDict(rule_obj)

    rules.append(rule)

    for field in EXPLODE_FIELDS:
        field_value = rule_obj.get(field)
        tmp_rules = []

        for value in field_value.split("&"):
            if value == '':
                continue

            for new_rule in rules:
                new_tmp_rule = copy.deepcopy(new_rule)
                setattr(new_tmp_rule, field, value)
                tmp_rules.append(new_tmp_rule)

        rules = tmp_rules

    rules = _generate_rule(rules)

    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')

    _insert(rules, chain)

"""
    try:
        chain.insert_rule(rule)
    except Exception as ex:
        raise InsertException( str(ex) )
"""


def _insert(rules, chain):
    for rule in rules:
        try:
            chain.insert_rule(rule)
        except InsertException:
            print "Insertion failed for the rule %s" %( str(rule) )
            import sys
            sys.exit(0)


if __name__ == "__main__":
    ins = {"src": "2.2.2.2", "protocol": "tcp&udp", "dst":"5.5.5.5", "target": "ACCEPT"}
    insert_input(ins)
    c = ConfigDict(ins)

"""
  lm = ConfigList()
    lm.append(2)
    lm.append(3)
    lm.append(4)
lm.append(6)
print lm[1:3]
"""





