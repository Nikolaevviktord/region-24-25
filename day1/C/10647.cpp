#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct segmentTree {
    ll l, r;
    ll sum = 0;
    segmentTree * k1 = 0, * k2 = 0;

    segmentTree(ll lr, ll rr, ll * a) {
        l = lr;
        r = rr;
        if (lr == rr - 1) {
            sum = a[l];
        } else {
            ll m = (l + r) / 2;
            k1 = new segmentTree(l, m, a);
            k2 = new segmentTree(m, r, a);
            sum = max(k1->sum, k2->sum);
        }
    }

    ll get(ll lq, ll rq) {
//        cout << lq + 1 << " " << rq << " " << l + 1 << " " << r << endl;
        if (l >= lq && r <= rq) {
            return sum;
        } else if (lq >= r || rq <= l) {
            return 0;
        } else {//if (k1) {
            return max(k1->get(lq, rq), k2->get(lq, rq));
        } return 0;
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n;
    cin >> n;

    ll a[n];
    for (ll i = 0; i < n; ++i) cin >> a[i];

    segmentTree maxt(0, n, a);

    vector<pair<ll, ll>> b(n);
    for (ll i = 0; i < n; ++i) b[i] = {i, i + 1};

    for (ll _ = 0; _ < n - 1; _++) {
        ll q;
        cin >> q;

        --q;

        b[q].second = b[q + 1].second;
        b.erase(b.begin() + q + 1);

//        cout << b[q].first + 1 << " " << b[q].second << endl;

        ll res = 0;
        for (ll i = b[q].first + 1; i < b[q].second - 1; ++i) {
//            cout << i + 1 << endl;
            res += max(0ll, min(maxt.get(b[q].first, i), maxt.get(i + 1, b[q].second)) - a[i]);
        }

        cout << res << "\n";
    }

    return 0;
}
