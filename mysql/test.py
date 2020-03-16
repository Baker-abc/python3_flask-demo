

if __name__ == '__main__':
    ips = ""
    count = 19
    end = 30
    while count < end:
        count += 1
        ips = ips + '172.20.0.' + str(count)
        if count != end:
            ips = ips + ','

    print(ips)