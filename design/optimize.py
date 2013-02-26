from layout import Layout

l = Layout()
mn = l.metric
i = 0
while True:
    i += 1
    l.shuffle()
    if not i % 1000:
        print '\r%s' % i,
    if l.metric < mn:
        mn = l.metric
        print 'New min: %s\n%s' % (mn, l)

