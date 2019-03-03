import requests

headers = {
    'Cookie': 'zap=11b9887e-d554-408d-b088-b2ca42f1a0bf; d_c0="AMBhkw0hxw6PTnKZ-i00f1P4usPAss7bxdA=|1546661497"; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; l_n_c=1; q_c1=8329f77c9b4a46308aa67dd430f00075|1550816096000|1546661498000; _xsrf=29378e4716611cc47f5e5022b8c95864; r_cap_id="NjA1ZjJjNTFhNjMyNGUyYWFkNGFkYjYwZGUwZjNiOWI=|1550816096|9e7553c9e774c30b61753589f32e9efd2a9f677c"; cap_id="NTMzYjk1NTI4ZDA3NGU3OWJjNzkyZGJkZGRmMjI1MDg=|1550816096|0faa9cdea9d09e3a32fe7e551a1e43b7d13ed12a"; l_cap_id="YjE4Y2ZmMjNmMTNjNDkzNTgzZmE5ODhkZmIxZGYwNGY=|1550816096|2ec06df308dfb308ff216e9002447da992f0d39f"; n_c=1; __utma=51854390.1568135277.1550816099.1550816099.1550816099.1; __utmb=51854390.0.10.1550816099; __utmc=51854390; __utmz=51854390.1550816099.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|3=entry_date=20190105=1; _xsrf=jrLBXyOicoY1bCNGnlb4Ssp3kiySi6Fy; tst=f; capsion_ticket="2|1:0|10:1550816702|14:capsion_ticket|44:MGEwYmMxODk5NDhmNGI1MWI2ZmZjN2EyMjNkMzU4MGE=|da689532626a76243d5407d7fa1cd57541396c21ea22ab8a5ce56dc815a01ba1"; z_c0="2|1:0|10:1550816719|4:z_c0|92:Mi4xVVpUY0F3QUFBQUFBd0dHVERTSEhEaVlBQUFCZ0FsVk56LU5jWFFBeThQemZCRnNib19VazJBNEhjbEotMkh5VU5n|354708a9cd24359bc3c5e499a6dfaabab78c1478bed2df97deff6c51b5f525f1"',
    'Host': 'www.zhihu.com',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 '
    #             '(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',

}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
