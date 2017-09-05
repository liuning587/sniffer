from builtins import Exception, str
from result.models import SnifferResult


def resultC():
    # 查询出全部可执行测试用例
    # sniffer=SnifferCases.objects.filter(state='1')
    # sniffer=sniffer.values("casename").distinct()
    # for e in sniffer:
    #     print(e['casename'])
    # 查询执行用例结果
    # resultsniffer = SnifferResult.objects.filter(casename = sniffer )
    # print(resultsniffer)
#     snifferRe = SnifferResult.objects.raw('''select r.id,c.id,c.casename, c.state,r.`RESULT` ,c.create_by,c.`SYSTEM`,c.url   ,from_unixtime(r.create_at) as create_at
# from sniffer.sniffer_cases c
# left  join(
# select id, cases_id, max(create_at) create_at from sniffer.sniffer_result  group by cases_id
# ) t on t.cases_id = c.id
# left join(   sniffer.sniffer_result r ) on r.cases_id=t.cases_id and t.create_at=r.create_at
# where c.state=1
# order by c.`SYSTEM`
# ''')
    time='很遗憾！都还没开始'
    snifferRe = SnifferResult.objects.raw('''
    select c.id,c.casename, c.state,t.`RESULT` ,c.create_by,c.`SYSTEM`,c.url ,t.create_at
    from sniffer_dev.sniffer_cases c
    left  join  sniffer_dev.sniffer_result  t
    on t.cases_id = c.id
    where c.state=1
    order by c.`SYSTEM`
    ''')
    resultCS={}
    for c in snifferRe:
        resutrc ={
            'id':c.id,
            'cname':c.casename,
            'result':c.RESULT,
            'url':c.url,
            'system':c.SYSTEM,
            'create_at':c.create_at
        }
        resultCS[c.SYSTEM] = resultCS.get(c.SYSTEM, [])
        resultCS[c.SYSTEM].append(resutrc)
        if c.create_at is not None:
            time=c.create_at
    resultCS['time']=time
    # snifferRe = json.dumps(snifferRe, cls=DjangoJSONEncoder)
    return resultCS