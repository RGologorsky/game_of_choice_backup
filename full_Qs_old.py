S8 return np.asarray([
            [
                f(xcc, ycc)*pcc*qcc, \
                f(xcc, ycc)*pcc*(1 - qcc), \
                f(xcc, ycc)*(1 - pcc)*qcc, \
                f(xcc, ycc)*(1 - pcc)*(1 - qcc), \
                (1 - f(xcc, ycc))*pcc* qcc, \
                (1 - f(xcc, ycc))*pcc* (1 - qcc), \
                (1 - f(xcc, ycc))* (1 - pcc)*qcc, \
                (1 - f(xcc, ycc))* (1 - pcc)* (1 - qcc) \
            ],

            [
                f(xcd, ydc)*pcd*qdc, \
                f(xcd, ydc)*pcd*(1 - qdc), \
                f(xcd, ydc)*(1 - pcd)*qdc, \
                f(xcd, ydc)*(1 - pcd)*(1 - qdc), \
                (1 - f(xcd, ydc))*pcd*qdc, \
                (1 - f(xcd, ydc))*pcd*(1 - qdc), \
                (1 - f(xcd, ydc))*(1 - pcd)*qdc, \
                (1 - f(xcd, ydc))*(1 - pcd)*(1 - qdc), \
            ],

            [
                f(xdc, ycd)*pdc*qcd, \
                f(xdc, ycd)*pdc*(1 - qcd), \
                f(xdc, ycd)* (1 - pdc)*qcd, \
                f(xdc, ycd)*(1 - pdc)*(1 - qcd), \
                (1 - f(xdc, ycd))*pdc*qcd, \
                (1 - f(xdc, ycd))*pdc*(1 - qcd), \
                (1 - f(xdc, ycd))*(1 - pdc)* qcd, \
                (1 - f(xdc, ycd))*(1 - pdc)*(1 - qcd), \
            ],

            [
                f(xdd, ydd)*pdd*qdd, \
                f(xdd, ydd)*pdd*(1 - qdd), \
                f(xdd, ydd)*(1 - pdd)*qdd, \
                f(xdd, ydd)*(1 - pdd)*(1 - qdd), \
                (1 - f(xdd, ydd))*pdd*qdd, \
                (1 - f(xdd, ydd))*pdd*(1 - qdd), \
                (1 - f(xdd, ydd))*(1 - pdd)*qdd, \
                (1 - f(xdd, ydd))*(1 - pdd)*(1 - qdd), \
            ],

            [
                f(xcc, ycc)*pcc*qcc, \
                f(xcc, ycc)*pcc*(1 - qcc), \
                f(xcc, ycc)*(1 - pcc)*qcc, \
                f(xcc, ycc)*(1 - pcc)*(1 - qcc), \
                (1 - f(xcc, ycc))*pcc* qcc, \
                (1 - f(xcc, ycc))*pcc* (1 - qcc), \
                (1 - f(xcc, ycc))* (1 - pcc)*qcc, \
                (1 - f(xcc, ycc))* (1 - pcc)* (1 - qcc), \
            ],

            [
                f(xcd, ydc)*pcd*qdc, \
                f(xcd, ydc)*pcd*(1 - qdc), \
                f(xcd, ydc)*(1 - pcd)*qdc, \
                f(xcd, ydc)*(1 - pcd)*(1 - qdc), \
                (1 - f(xcd, ydc))*pcd*qdc, \
                (1 - f(xcd, ydc))*pcd*(1 - qdc), \
                (1 - f(xcd, ydc))*(1 - pcd)*qdc, \
                (1 - f(xcd, ydc))*(1 - pcd)*(1 - qdc), \
            ],

            [
                f(xdc, ycd)*pdc*qcd, \
                f(xdc, ycd)*pdc*(1 - qcd), \
                f(xdc, ycd)* (1 - pdc)*qcd, \
                f(xdc, ycd)*(1 - pdc)*(1 - qcd), \
                (1 - f(xdc, ycd))*pdc*qcd, \
                (1 - f(xdc, ycd))*pdc*(1 - qcd), \
                (1 - f(xdc, ycd))*(1 - pdc)* qcd, \
                (1 - f(xdc, ycd))*(1 - pdc)*(1 - qcd), \
            ],

            [
                f(xdd, ydd)*pdd*qdd, \
                f(xdd, ydd)*pdd*(1 - qdd), \
                f(xdd, ydd)*(1 - pdd)*qdd, \
                f(xdd, ydd)*(1 - pdd)*(1 - qdd), \
                (1 - f(xdd, ydd))*pdd*qdd, \
                (1 - f(xdd, ydd))*pdd*(1 - qdd), \
                (1 - f(xdd, ydd))*(1 - pdd)*qdd, \
                (1 - f(xdd, ydd))*(1 - pdd)*(1 - qdd), \
            ]
        ]);


S12 return np.asarray([
            [
                f(xcc, ycc)*p1cc*q1cc, \
                f(xcc, ycc)*p1cc*(1 - q1cc), \
                f(xcc, ycc)*(1 - p1cc)*q1cc, \
                f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
                (1 - f(xcc, ycc))*p2cc* q2cc, \
                (1 - f(xcc, ycc))*p2cc* (1 - q2cc), \
                (1 - f(xcc, ycc))* (1 - p2cc)*q2cc, \
                (1 - f(xcc, ycc))* (1 - p2cc)* (1 - q2cc) \
            ],

            [
                f(xcd, ydc)*p1cd*q1dc, \
                f(xcd, ydc)*p1cd*(1 - q1dc), \
                f(xcd, ydc)*(1 - p1cd)*q1dc, \
                f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
                (1 - f(xcd, ydc))*p2cd*q2dc, \
                (1 - f(xcd, ydc))*p2cd*(1 - q2dc), \
                (1 - f(xcd, ydc))*(1 - p2cd)*q2dc, \
                (1 - f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                f(xdc, ycd)*p1dc*q1cd, \
                f(xdc, ycd)*p1dc*(1 - q1cd), \
                f(xdc, ycd)* (1 - p1dc)*q1cd, \
                f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
                (1 - f(xdc, ycd))*p2dc*q2cd, \
                (1 - f(xdc, ycd))*p2dc*(1 - q2cd), \
                (1 - f(xdc, ycd))*(1 - p2dc)* q2cd, \
                (1 - f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                f(xdd, ydd)*p1dd*q1dd, \
                f(xdd, ydd)*p1dd*(1 - q1dd), \
                f(xdd, ydd)*(1 - p1dd)*q1dd, \
                f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
                (1 - f(xdd, ydd))*p2dd*q2dd, \
                (1 - f(xdd, ydd))*p2dd*(1 - q2dd), \
                (1 - f(xdd, ydd))*(1 - p2dd)*q2dd, \
                (1 - f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
            ],

            [
                f(xcc, ycc)*p1cc*q1cc, \
                f(xcc, ycc)*p1cc*(1 - q1cc), \
                f(xcc, ycc)*(1 - p1cc)*q1cc, \
                f(xcc, ycc)*(1 - p1cc)*(1 - q1cc), \
                (1 - f(xcc, ycc))*p2cc* q2cc, \
                (1 - f(xcc, ycc))*p2cc* (1 - q2cc), \
                (1 - f(xcc, ycc))* (1 - p2cc)*q2cc, \
                (1 - f(xcc, ycc))* (1 - p2cc)* (1 - q2cc), \
            ],

            [
                f(xcd, ydc)*p1cd*q1dc, \
                f(xcd, ydc)*p1cd*(1 - q1dc), \
                f(xcd, ydc)*(1 - p1cd)*q1dc, \
                f(xcd, ydc)*(1 - p1cd)*(1 - q1dc), \
                (1 - f(xcd, ydc))*p2cd*q2dc, \
                (1 - f(xcd, ydc))*p2cd*(1 - q2dc), \
                (1 - f(xcd, ydc))*(1 - p2cd)*q2dc, \
                (1 - f(xcd, ydc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                f(xdc, ycd)*p1dc*q1cd, \
                f(xdc, ycd)*p1dc*(1 - q1cd), \
                f(xdc, ycd)* (1 - p1dc)*q1cd, \
                f(xdc, ycd)*(1 - p1dc)*(1 - q1cd), \
                (1 - f(xdc, ycd))*p2dc*q2cd, \
                (1 - f(xdc, ycd))*p2dc*(1 - q2cd), \
                (1 - f(xdc, ycd))*(1 - p2dc)* q2cd, \
                (1 - f(xdc, ycd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                f(xdd, ydd)*p1dd*q1dd, \
                f(xdd, ydd)*p1dd*(1 - q1dd), \
                f(xdd, ydd)*(1 - p1dd)*q1dd, \
                f(xdd, ydd)*(1 - p1dd)*(1 - q1dd), \
                (1 - f(xdd, ydd))*p2dd*q2dd, \
                (1 - f(xdd, ydd))*p2dd*(1 - q2dd), \
                (1 - f(xdd, ydd))*(1 - p2dd)*q2dd, \
                (1 - f(xdd, ydd))*(1 - p2dd)*(1 - q2dd), \
            ]
        ])


S16 return np.asarray([
            [
                f(x1cc, y1cc)*p1cc*q1cc, \
                f(x1cc, y1cc)*p1cc*(1 - q1cc), \
                f(x1cc, y1cc)*(1 - p1cc)*q1cc, \
                f(x1cc, y1cc)*(1 - p1cc)*(1 - q1cc), \
                (1 - f(x1cc, y1cc))*p2cc* q2cc, \
                (1 - f(x1cc, y1cc))*p2cc* (1 - q2cc), \
                (1 - f(x1cc, y1cc))* (1 - p2cc)*q2cc, \
                (1 - f(x1cc, y1cc))* (1 - p2cc)* (1 - q2cc) \
            ],

            [
                f(x1cd, y1dc)*p1cd*q1dc, \
                f(x1cd, y1dc)*p1cd*(1 - q1dc), \
                f(x1cd, y1dc)*(1 - p1cd)*q1dc, \
                f(x1cd, y1dc)*(1 - p1cd)*(1 - q1dc), \
                (1 - f(x1cd, y1dc))*p2cd*q2dc, \
                (1 - f(x1cd, y1dc))*p2cd*(1 - q2dc), \
                (1 - f(x1cd, y1dc))*(1 - p2cd)*q2dc, \
                (1 - f(x1cd, y1dc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                f(x1dc, y1cd)*p1dc*q1cd, \
                f(x1dc, y1cd)*p1dc*(1 - q1cd), \
                f(x1dc, y1cd)* (1 - p1dc)*q1cd, \
                f(x1dc, y1cd)*(1 - p1dc)*(1 - q1cd), \
                (1 - f(x1dc, y1cd))*p2dc*q2cd, \
                (1 - f(x1dc, y1cd))*p2dc*(1 - q2cd), \
                (1 - f(x1dc, y1cd))*(1 - p2dc)* q2cd, \
                (1 - f(x1dc, y1cd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                f(x1dd, y1dd)*p1dd*q1dd, \
                f(x1dd, y1dd)*p1dd*(1 - q1dd), \
                f(x1dd, y1dd)*(1 - p1dd)*q1dd, \
                f(x1dd, y1dd)*(1 - p1dd)*(1 - q1dd), \
                (1 - f(x1dd, y1dd))*p2dd*q2dd, \
                (1 - f(x1dd, y1dd))*p2dd*(1 - q2dd), \
                (1 - f(x1dd, y1dd))*(1 - p2dd)*q2dd, \
                (1 - f(x1dd, y1dd))*(1 - p2dd)*(1 - q2dd), \
            ],

            [
                f(x2cc, y2cc)*p1cc*q1cc, \
                f(x2cc, y2cc)*p1cc*(1 - q1cc), \
                f(x2cc, y2cc)*(1 - p1cc)*q1cc, \
                f(x2cc, y2cc)*(1 - p1cc)*(1 - q1cc), \
                (1 - f(x2cc, y2cc))*p2cc* q2cc, \
                (1 - f(x2cc, y2cc))*p2cc* (1 - q2cc), \
                (1 - f(x2cc, y2cc))* (1 - p2cc)*q2cc, \
                (1 - f(x2cc, y2cc))* (1 - p2cc)* (1 - q2cc), \
            ],

            [
                f(x2cd, y2dc)*p1cd*q1dc, \
                f(x2cd, y2dc)*p1cd*(1 - q1dc), \
                f(x2cd, y2dc)*(1 - p1cd)*q1dc, \
                f(x2cd, y2dc)*(1 - p1cd)*(1 - q1dc), \
                (1 - f(x2cd, y2dc))*p2cd*q2dc, \
                (1 - f(x2cd, y2dc))*p2cd*(1 - q2dc), \
                (1 - f(x2cd, y2dc))*(1 - p2cd)*q2dc, \
                (1 - f(x2cd, y2dc))*(1 - p2cd)*(1 - q2dc), \
            ],

            [
                f(x2dc, y2cd)*p1dc*q1cd, \
                f(x2dc, y2cd)*p1dc*(1 - q1cd), \
                f(x2dc, y2cd)* (1 - p1dc)*q1cd, \
                f(x2dc, y2cd)*(1 - p1dc)*(1 - q1cd), \
                (1 - f(x2dc, y2cd))*p2dc*q2cd, \
                (1 - f(x2dc, y2cd))*p2dc*(1 - q2cd), \
                (1 - f(x2dc, y2cd))*(1 - p2dc)* q2cd, \
                (1 - f(x2dc, y2cd))*(1 - p2dc)*(1 - q2cd), \
            ],

            [
                f(x2dd, y2dd)*p1dd*q1dd, \
                f(x2dd, y2dd)*p1dd*(1 - q1dd), \
                f(x2dd, y2dd)*(1 - p1dd)*q1dd, \
                f(x2dd, y2dd)*(1 - p1dd)*(1 - q1dd), \
                (1 - f(x2dd, y2dd))*p2dd*q2dd, \
                (1 - f(x2dd, y2dd))*p2dd*(1 - q2dd), \
                (1 - f(x2dd, y2dd))*(1 - p2dd)*q2dd, \
                (1 - f(x2dd, y2dd))*(1 - p2dd)*(1 - q2dd), \
            ]
        ])
