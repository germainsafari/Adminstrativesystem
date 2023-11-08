import pickle

def save_users():
    with open('users.pkl, wb') as f:
        pickle.dump(users_list, f)
def load_users():
    with open('users.pkl', 'rb') as f:
        users_list = pickle.load(f)