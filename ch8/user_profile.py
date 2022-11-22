#Using Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

#Try it yourself
def sandwich(lists):
    """Return a neatly formatted summary of sandwiches."""
    for list in lists:
        print(f"Hey, kindly wait for your {list} order come 2023.")
    
a = ['cassava', 'garri', 'agbado', 'ewa']
sandwich(a)

user_profile = build_profile('Ebuka', 'Ihekwereme', location='lagos', field='accounting')
print(user_profile)
