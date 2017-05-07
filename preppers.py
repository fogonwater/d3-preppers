import json

class D3graph:
    def __init__(self):
        self.nodes = {}
        self.links = []

    def upsert_node(self, _id, value=0, static_attributes={}):
        """
        Update an existing node, or create a new one. Only the
        "value" property will be incremented.
        """
        nodes = self.nodes

        # If no value supplied, but one appears in static_attributes,
        # use the static_attributes instead. This is probably a dumb idea.
        if not value and 'value' in static_attributes:
            value = float(static_attributes['value'])

        # If no node exists, create a new node one with a value.
        if not _id in nodes:
            nodes[_id] = {'id':_id, 'value': value}
        # Otherwise increment the existing value
        else:
            nodes[_id]['value'] += value

        # Use static_attributes to set other node attributes
        # Overrides existing key:values with most recently received
        for k, v in static_attributes.items():
            # Ignore any key named 'value'.
            if k == 'value':
                continue
            nodes[_id][k] = v

    def add_link(self, source, target, value=0, static_attributes={}):
        """
        Add a new source -> target link, with optional attributes.
        Updates nodes along the way, creating new ones if necessary
        """
        self.upsert_node(source, value=value)
        self.upsert_node(target, value=value)
        base_link = {'source':source,'target':target, 'value': value}

        # remove any dangerous key:values from static_attributes
        # TODO - this shouldn't happen silently
        static_attributes.pop("source", None)
        static_attributes.pop("target", None)
        static_attributes.pop("value", None)

        # combine base_link and any static_attributes
        self.links.append( dict(base_link.items() + static_attributes.items()) )

    def export(self, f_path):
        """ Export the nodes and values to a D3 JSON file """
        report = {'nodes':self.nodes.values(), 'links':self.links}
        with open(f_path, 'w') as outfile:
            json.dump(
                report,
                outfile,
                indent=2,
                #sort_keys=True
            )
        print('{} written.'.format(f_path))


def test():
    g = D3graph()
    data = [
        ['a','b',5],
        ['a','c',5],
        ['b','c',5],
        ['c','d',10],
        ['c','e',10],
        ['f','a',10],
        ['g','a',10],
        ['f','b',10],
        ['g','c',10],
    ]
    for row in data:
        g.add_link(row[0], row[1], row[2])
    g.export('test.json')

def main():
    test()

if __name__ == '__main__':
    main()
