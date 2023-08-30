def parse_int(string):
    nums = {'':0, 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11,
        'twelve':12, 'thirteen':13, 'fifteen':15, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50}
    multiplier = {'trillion':1000000000000, 'billion':1000000000, 'million':1000000, 'thousand':1000}
    list1 = ['trillion', 'billion', 'million', 'thousand']

    sum =  0
    try:
        for i in list1:
            if i in string:
                new = string.split(i, 1)
                string = new[-1]
                if 'hundred' in new[0]:
                    x = new[0].split('hundred')
                    sum += nums[x[0].strip()] * 100 * multiplier[i]
                    if ' ' in x[-1].strip():
                        y = x[-1].strip().split(' ')
                        if 'ty' in y[0].strip() and y[0].strip() != 'twenty' and y[0].strip() != 'thirty' and y[0].strip() != 'forty' and y[0].strip() != 'fifty':
                            sum += ((nums[y[0][:-2]] * 10) + nums[y[-1]]) * multiplier[i]
                        else:
                            sum += (nums[y[0].strip()] + nums[y[-1].strip()]) * multiplier[i]
                    else:
                        if 'teen' in x[-1].strip() and x[-1].strip() != 'thirteen' and x[-1].strip() != 'fifteen':
                            sum += (10 + nums[x[-1].strip()[:-4]]) * multiplier[i]
                        elif 'ty' in x[-1].strip() and x[-1].strip() != 'twenty' and x[-1].strip() != 'thirty' and x[-1].strip() != 'forty' and x[-1].strip() != 'fifty':
                            sum += (nums[x[-1].strip()[:-2]] * 10) * multiplier[i]
                        else:
                            sum += nums[x[-1].strip()] * multiplier[i]
                elif not 'hundred' in new[0].strip():
                    if ' ' in new[0].strip():
                        y = new[0].strip().split(' ')
                        if 'ty' in y[0].strip() and y[0].strip() != 'twenty' and y[0].strip() != 'thirty' and y[0].strip() != 'forty' and y[0].strip() != 'fifty':
                            sum += ((nums[y[0].strip()[:-2]] * 10) + nums[y[-1].strip()]) * multiplier[i]
                        else:
                            sum += (nums[y[0].strip()] + nums[y[-1].strip()]) * multiplier[i]
                    else:
                        if 'teen' in new[0].strip() and new[0].strip() != 'thirteen' and new[0].strip() != 'fifteen':
                            sum += (10 + nums[new[0].strip()[:-4]]) * multiplier[i]
                        elif 'ty' in new[0].strip() and new[0].strip() != 'twenty' and new[0].strip() != 'thirty' and new[0].strip() != 'forty' and new[0].strip() != 'fifty':
                            sum += (nums[new[0].strip()[:-2]] * 10) * multiplier[i]
                        else:
                            sum += nums[new[0].strip()] * multiplier[i]
            else:
                pass
        
        if 'hundred' in string and string.split().count('hundred') == 1:
            x = string.split('hundred')
            sum += nums[x[0].strip()] * 100
            if ' ' in x[-1].strip():
                y = x[-1].strip().split(' ')
                if 'ty' in y[0].strip() and y[0].strip() != 'twenty' and y[0].strip() != 'thirty' and y[0].strip() != 'forty' and y[0].strip() != 'fifty':
                    sum += ((nums[y[0].strip()[:-2]] * 10) + nums[y[-1].strip()])
                elif y[0].strip() == 'forty':
                    sum += (nums[y[0].strip()] + nums[y[-1].strip()])
                else:
                    sum += nums[y[0].strip()] + nums[y[-1].strip()]
            else:
                if 'teen' in x[-1].strip() and x[-1].strip() != 'thirteen' and x[-1].strip() != 'fifteen':
                    sum += (10 + nums[x[-1].strip()[:-4]])
                elif 'ty' in x[-1].strip() and x[-1].strip() != 'twenty' and x[-1].strip() != 'thirty' and x[-1].strip() != 'forty' and x[-1].strip() != 'fifty':
                    sum += (nums[x[-1].strip()[:-2]] * 10)
                else:
                    sum += nums[x[-1].strip()]
        elif ' ' in string.strip() and not 'hundred' in string:
            y = string.strip().split(' ')
            if 'ty' in y[0].strip() and y[0].strip() != 'twenty' and y[0].strip() != 'thirty' and y[0].strip() != 'forty' and y[0].strip() != 'fifty':
                sum += ((nums[y[0].strip()[:-2]] * 10) + nums[y[-1].strip()])
            else:
                sum += nums[y[0].strip()] + nums[y[-1].strip()]
        else:
            if 'teen' in string.strip() and string.strip() != 'thirteen' and string.strip() != 'fifteen':
                sum += (10 + nums[string.strip()[:-4]])
            elif 'ty' in string.strip() and string.strip() != 'twenty' and string.strip() != 'thirty' and string.strip() != 'forty' and string.strip() != 'fifty':
                sum += (nums[string.strip()[:-2]] * 10)
            else:
                sum += nums[string.strip()]
        return sum
    except KeyError:
        print('You entered a wrong number spelling.')
        return ''


if __name__ == '__main__':
    string = input('Enter your number in words: ').replace(' and', '').replace(',', '').replace('-', ' ')
    print(parse_int(string))