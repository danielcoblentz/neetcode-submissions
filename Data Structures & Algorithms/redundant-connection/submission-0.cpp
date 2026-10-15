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

    bool unite(int a, int b){
        a = find(a), b = find(b);
        if (a == b) return false;
        if (s[a] < s[b]) swap(a, b);
        p[b] = p[a];
        s[a] += s[b];
        comps --;
        return true;
    }
};






class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UnionFind uf(edges.size());
        for (const auto& e : edges) {
            if (!uf.unite(e[0], e[1])) return {e[0], e[1]};
        }        
        return {};
    }
};
