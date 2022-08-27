from framework.elements.base.base_element import BaseElement


class Table(BaseElement):

    def __init__(self, search_condition, locator, name):
        super(Table, self).__init__(search_condition_of=search_condition, loc=locator, name_of=name)

    def all_lines(self):
        lines = list()
        for elem in self.get_elements():
            lines.append(elem.text)
        return lines

    def get_cloumn_data(self, data_type):
        names = list()
        if data_type == 'test name':
            number = 1
        if data_type == 'test time':
            number = 4
        names_path = BaseElement('xpath',
                                 f'//table[@class="table"]/tbody/tr/td[{number}]',
                                 'names')
        for name in names_path.get_elements():
            names.append(name.text)
        return names

    def row_count(self):
        return len(self.get_elements())
