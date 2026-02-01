from models import User
from models import Question
from models import Thread
from models import Anonymous

users_dict = {}

class UserServices():
    counter = 0

    def add_user(self ,name , password, email , allow_anonymous):
        u = User(name , password, email , allow_anonymous)
        users_dict[u.getId()] = u
        UserServices.counter +=1


class QuestionServices():
    def AskQuestion(self ,from_user_id , to_user_id , value):
        Q = Question(from_user_id , to_user_id , value)

        from_user_obj = users_dict[from_user_id]
        to_user_obj = users_dict[to_user_id]

        from_user_obj.from_me_q[Q.parent_id] = [Q.to_user_id ,value , Q.answered  ]

    def AQ(self ,from_user_id , to_user_id , value):
        AQ = Anonymous(self ,from_user_id , to_user_id , value)
        from_user_obj = users_dict[from_user_id]
        to_user_obj = users_dict[to_user_id]

        from_user_obj.from_me_q[AQ.parent_id] = [AQ.to_user_id ,value , AQ.answered  ]
        pass

    def thread(self ,from_user_id , to_user_id , value):
        T = Thread(self ,from_user_id , to_user_id , value)
        from_user_obj = users_dict[from_user_id]
        to_user_obj = users_dict[to_user_id]

        from_user_obj.from_me_q[T.parent_id] = [T.to_user_id ,value , T.answered  ]
        pass
    pass
