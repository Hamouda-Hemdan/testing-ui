from flask import Flask, request, render_template
from collections import defaultdict, deque

app = Flask(__name__)

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(numCourses)}

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque([i for i in indegree if indegree[i] == 0])

    count = 0
    while queue:
        node = queue.popleft()
        count += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return count == numCourses

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numCourses = int(request.form['numCourses'])
        prerequisites = eval(request.form['prerequisites'])
        result = canFinish(numCourses, prerequisites)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
