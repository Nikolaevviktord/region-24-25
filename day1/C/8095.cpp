#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct segment {
    vector<ll> h;

    ll cnt() {
        ll res = 0;

        for (ll i = 1; i < h.size() - 1; ++i) {
            ll mxl = *max_element(h.begin(), h.begin() + i);
            ll mxr = *max_element(h.begin() + i, h.end());

            res += max(0ll, min(mxl, mxr) - h[i]);
        } return res;
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n;
    cin >> n;

    vector<segment> a(n);
    for (ll i = 0; i < n; ++i) {
        ll v;
        cin >> v;
        a[i].h.push_back(v);
    }

    n -= 1;
    while (n--) {
        ll q;
        cin >> q;

        --q;

        for (auto i: a[q + 1].h) a[q].h.push_back(i);
        a.erase(a.begin() + q + 1);

        cout << a[q].cnt() << "\n";
    }

    return 0;
}
