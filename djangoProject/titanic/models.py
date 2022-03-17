from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):

    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis = 1)
        this = self.drop_feature(this,'SibSp','Parch','Cabin','Ticket')
        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train 의 타입  {type(this.train)}')
        ic(f'2. Train 의 컬럼  {this.train.columns}')
        ic(f'3. Train 의 상위 1개  {this.train.head(1)}')
        ic(f'4. Train 의 null의 개수  {this.train.isnull().sum()}')
        ic(f'5. Test 의 타입  {type(this.test)}')
        ic(f'6. Test 의 컬럼  {this.test.columns}')
        ic(f'7. Test 의 상위 1개  {this.test.head(1)}')
        ic(f'8. Test 의 null의 개수  {this.test.isnull().sum()}')
        ic(f'9. id 의 타입  {type(this.id)}')
        ic(f'10. id 의 상위 3개 {this.id[:3]}')
        print('*' * 100)
    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)

        # a = [i for i in []]
        # this.train = this.train.drop('SibSp', axis=1)
        # this.train = this.train.drop('Parch', axis=1)
        # this.train = this.train.drop('Cabin', axis=1)
        # this.train = this.train.drop('Ticket', axis=1)

        # this.test = this.test.drop('SibSp', axis=1)
        # this.test = this.test.drop('Parch', axis=1)
        # this.test = this.test.drop('Cabin', axis=1)
        # this.test = this.test.drop('Ticket', axis=1)

        '''
        self.cabin_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.sib_sp_garbage(df)
        '''
        return this
    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(this)->object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this)->object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this