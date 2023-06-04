def get_topics():
    topics = []
    with open('./keys.txt', 'r') as file:
        for line in file.readlines():
            if '-' in line:
                key = line.replace('- ', '').strip()
                topics.append(key)
        
    print(f'{__name__}: {topics}')

    return topics

if __name__ == '__main__':
    topics = get_topics()