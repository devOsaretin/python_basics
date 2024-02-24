# def post(fn):
#     def func_wrapper():
        
#         print ("Here I will make a post request with the passed function")
#         fn()
#     return func_wrapper

# @post
# def make_post(request):
#     print(request)



def post(fn):
    def func_wrapper(*args, **kwargs):
        print("Here I will make a post request with the passed function")
        fn(*args, **kwargs)
    return func_wrapper

@post
def make_post(request):
    print(request)

make_post("Sample request data")