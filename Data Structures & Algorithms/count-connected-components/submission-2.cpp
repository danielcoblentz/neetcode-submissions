class UnionFind {
    public:
    vector<int> p, s;
    int comps;

    UnionFind(int n) : p(n + 1), s(n + 1, 1), comps(n) {
        iota(p.begin(), p.end(), 0);
    }

    int find(int x) {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    int unite(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (s[a] < s[b]) swap(a, b);
        p[b] = a;
        s[a] += s[b];
        comps--;
        return true;
    }
};


class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        UnionFind uf(n);
        for (const auto& e : edges) {
            uf.unite(e[0],e[1]);
        }
        return uf.comps;

    }
};
