class MyHashSet {
public:
    vector<bool> seen;
    MyHashSet() : seen(1000001, false) {
    }
    
    void add(int key) {
        seen[key] = true;
    }
    
    void remove(int key) {
        seen[key] = false;
    }
    
    bool contains(int key) {
        return seen[key];
    }
};