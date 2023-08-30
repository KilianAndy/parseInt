def parse_int(string):
    nums = {'':0, 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11,
        'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
        'thirty':30, 'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
    multiplier = {'trillion':1000000000000, 'billion':1000000000, 'million':1000000, 'thousand':1000}
    list1 = ['trillion', 'billion', 'million', 'thousand']

    sum =  0
    string = string.replace(' and', '')
    string = string.replace('-', ' ')
    list1 = ['trillion', 'billion', 'million', 'thousand']
    for i in list1:
        if i in string:
            new = string.split(i, 1)
            string = new[-1]
            if 'hundred' in new[0]:
                x = new[0].split('hundred')
                sum += nums[x[0].strip()] * 100 * multiplier[i]
                if ' ' in x[-1].strip():
                    y = x[-1].strip().split(' ')
                    sum += (nums[y[0]] + nums[y[-1]]) * multiplier[i]
                else:
                    sum += nums[x[-1].strip()] * multiplier[i]
            elif not 'hundred' in new[0]:
                if ' ' in new[0].strip():
                    y = new[0].strip().split(' ')
                    sum += (nums[y[0]] + nums[y[-1]]) * multiplier[i]
                else:
                    sum += nums[new[0].strip()] * multiplier[i]
        else:
            pass

    
    if 'hundred' in string:
        x = string.split('hundred')
        sum += nums[x[0].strip()] * 100
        if ' ' in x[-1].strip():
            y = x[-1].strip().split(' ')
            sum += nums[y[0]] + nums[y[-1]]
        else:
            sum += nums[x[-1].strip()]
    elif ' ' in string.strip() and not 'hundred' in string:
        y = string.strip().split(' ')
        sum += nums[y[0]] + nums[y[-1]]
    else:
        sum += nums[string.strip()]
    return sum


if __name__ == '__main__':
    string = input('Enter your number in words: ').replace(' and', '').replace(',', '')
    print(parse_int(string))