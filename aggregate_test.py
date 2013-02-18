import aggregate
import unittest
from nose.tools import eq_

class agg_list_test(unittest.TestCase):
    '''example data of person, date, points'''
    data = [ ( 'Lilly', '2013-2-16', 50 ),
             ( 'Lilly', '2013-2-15', 20 ),
             ( 'Dad', '2013-2-16', 10 ),
             ( 'Dad', '2013-2-15', 10 ),
             ( 'Mom', '2013-2-16', 10 ) ]
    data_comment = 'these are rummy scores, or golf or something. Mom owns'

    def list_sum_test(self):
        data = self.data
        actual = aggregate.group(data, by=0, sum=2)
        Lilly = [person for person in actual if person[0]=='Lilly'][0]
        Mom = [person for person in actual if person[0]=='Mom'][0]
        Dad = [person for person in actual if person[0]=='Dad'][0]
        eq_( Lilly[1], 70)
        eq_( Dad[1], 20)
        eq_( Mom[1], 10)
        #assert [ ( 'Lilly', 70),
        #         ( 'Dad', 20),
        #         ( 'Mom', 10) ] == aggregate.group(data, by=0, sum=2)

    def list_count_test(self):
        data = self.data
        actual = aggregate.group(data, by=0, count=True)
        Lilly = [person for person in actual if person[0]=='Lilly'][0]
        Mom = [person for person in actual if person[0]=='Mom'][0]
        Dad = [person for person in actual if person[0]=='Dad'][0]
        eq_(2, Lilly[1])
        eq_(2, Dad[1])
        eq_(1, Mom[1])
        #assert [ ( 'Lilly', 2),
        #         ( 'Dad', 2),
        #         ( 'Mom', 1) ] == aggregate.group(data, by=0, count=True)

    def raises_on_out_of_range_sum_test(self):
        data = self.data
        try:
            aggregate.group(data, by=0, sum=3)
            raise
        except ValueError:
            pass

    def list_avg_test(self):
        data = self.data
        actual = aggregate.group(data, by=0, avg=2)
        Lilly = [person for person in actual if person[0]=='Lilly'][0]
        Mom = [person for person in actual if person[0]=='Mom'][0]
        Dad = [person for person in actual if person[0]=='Dad'][0]
        eq_( Lilly[1], 35)
        eq_( Dad[1], 10)
        eq_( Mom[1], 10)

    def list_max_test(self):
        data = self.data
        actual = aggregate.group(data, by=0, maxs=2)
        Lilly = [person for person in actual if person[0]=='Lilly'][0]
        Mom = [person for person in actual if person[0]=='Mom'][0]
        Dad = [person for person in actual if person[0]=='Dad'][0]
        eq_( Lilly[1], 50)
        eq_( Dad[1], 10)
        eq_( Mom[1], 10)

    def list_min_test(self):
        data = self.data
        actual = aggregate.group(data, by=0, mins=2)
        Lilly = [person for person in actual if person[0]=='Lilly'][0]
        Mom = [person for person in actual if person[0]=='Mom'][0]
        Dad = [person for person in actual if person[0]=='Dad'][0]
        eq_( Lilly[1], 20)
        eq_( Dad[1], 10)
        eq_( Mom[1], 10)

class group_dict_tests(unittest.TestCase):
    dict_data =[{ 'name' : 'Lilly', 'date' : 'blah', 'score' : 100 },
                { 'name' : 'Lilly', 'date' : 'blah', 'score' : 200 },
                { 'name' : 'Dad', 'date' : 'blah', 'score' : 10 },
                { 'name' : 'Mom', 'date' : 'blah', 'score' : 150 },
                { 'name' : 'Mom', 'date' : 'blah', 'score' : 300 } ]
    def sum_test(self):
        data = self.dict_data
        actual = aggregate.group(data, by='name', sum='score')
        Lilly = [person for person in actual if person['name']=='Lilly'][0]
        Mom = [person for person in actual if person['name']=='Mom'][0]
        Dad = [person for person in actual if person['name']=='Dad'][0]
        eq_( Lilly['sum(score)'], 300)
        eq_( Dad['sum(score)'], 10)
        eq_( Mom['sum(score)'], 450)

class morelist_group_tests(unittest.TestCase):
    data = [ [ 'a', 10, 100, 1000],
             [ 'a',  1, 200, 1100],
             [ 'a', 20, 300, 1124],
             [ 'b',  6,  50,   40],
             [ 'b', 20, 100,   22],]
    def mixed_aggregate_test(self):
        actual = aggregate.group(self.data, by=0, avg=[1,2,3], mins=[1,2,3], maxs=[1,2,3])
        eq_('a', actual[0][0])
        eq_('b', actual[1][0])
        eq_(31/3, actual[0][1])
        eq_(13, actual[1][1])
        eq_(200, actual[0][2])
        eq_(75, actual[1][2])
        eq_(3224/3, actual[0][3])
        eq_(31, actual[1][3])
        eq_(1, actual[0][4])
        eq_(6, actual[1][4])
        eq_(100, actual[0][5])
        eq_(50, actual[1][5])
        eq_(1000, actual[0][6])
        eq_(22, actual[1][6])
        eq_(20, actual[0][7])
        eq_(20, actual[1][7])
        eq_(300, actual[0][8])
        eq_(100, actual[1][8])
        eq_(1124, actual[0][9])
        eq_(40, actual[1][9])


class moredict_group_tests(unittest.TestCase):
    data = [ { 'name' : 'Joe', 'city' : 'Detroit', 'date': '2013-02-15', 'points' : 1000, 'errors' : 5 },
             { 'name' : 'Joe', 'city' : 'Detroit', 'date': '2013-02-16', 'points' : 1000, 'errors' : 0 },
             { 'name' : 'Bob', 'city' : 'Detroit', 'date': '2013-02-15', 'points' : 500, 'errors' : 0 },
             { 'name' : 'Jay', 'city' : 'Milan', 'date': '2013-02-15', 'points' : 5000, 'errors' : 0 },
             { 'name' : 'Jay', 'city' : 'Milan', 'date': '2013-02-16', 'points' : 5000, 'errors' : 0 },
             { 'name' : 'Janice', 'city' : 'Milan', 'date': '2013-02-15', 'points' : 15000, 'errors' : 0 },
             { 'name' : 'Janice', 'city' : 'Milan', 'date': '2013-02-16', 'points' : 15000, 'errors' : 0 },
             { 'name' : 'Ali', 'city' : 'Detroit', 'date': '2013-02-15', 'points' : 1500, 'errors' : 0 },
             ]
    def force_return_dict_test(self):
        actual = aggregate.group(self.data, by='city', avg='points', returnas='dict')
        Detroit = [i for i in actual if i['city']=='Detroit'][0]
        Milan = [i for i in actual if i['city']=='Milan'][0]
        eq_( 1000, Detroit['avg(points)'] )
        eq_( 10000, Milan['avg(points)'] )
    def force_return_list_test(self):
        actual = aggregate.group(self.data, by='city', avg='points', returnas='list')
        print(actual)
        Detroit = [i for i in actual if i[0]=='Detroit'][0]
        Milan = [i for i in actual if i[0]=='Milan'][0]
        eq_( 1000, Detroit[1] )
        eq_( 10000, Milan[1] )
    def avg_points_by_city_test(self):
        actual = aggregate.group(self.data, by='city', avg='points')
        print(actual)
        Detroit = [i for i in actual if i['city']=='Detroit'][0]
        Milan = [i for i in actual if i['city']=='Milan'][0]
        eq_( 1000, Detroit['avg(points)'] )
        eq_( 10000, Milan['avg(points)'] )

    def sum_points_by_city_test(self):
        actual = aggregate.group(self.data, by='city', sum='points')
        Detroit = [i for i in actual if i['city']=='Detroit'][0]
        Milan = [i for i in actual if i['city']=='Milan'][0]
        eq_( 4000, Detroit['sum(points)'] )
        eq_( 40000, Milan['sum(points)'] )
