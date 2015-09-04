class Subscriber(object):
    def __init__(self, **kwargs):
        defaults = {
            'email': None,
            'name': None,
            'date': None,
            'groups': None,
            'fields': None,
            'campaigns': None,
        }

        for (param, default) in defaults.iteritems():
            setattr(self, param, kwargs.get(param, default))

    def __str__(self):
        return self.AsJsonString()

    def AsJsonString(self):
        return json.dumps(self.AsDict(), sort_keys=True)

    def AsDict(self):
        data = {}

        if self.email:
            data['email'] = self.email
        if self.name:
            data['name'] = self.name
        if self.date:
            data['date'] = self.date
        if self.groups:
            data['groups'] = self.groups
        if self.fields:
            data['fields'] = self.fields
        if self.campaigns:
            data['campaigns'] = self.campaigns

        return data

    @staticmethod
    def _new_from_json_dict(data):
        return Campaign(
            email=data.get('email', None),
            name=data.get('name', None),
            date=data.get('date', None),
            groups=data.get('groups', None),
            fields=data.get('fields', None),
            campaigns=data.get('campaigns', None),
        )
