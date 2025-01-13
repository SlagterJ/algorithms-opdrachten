from graphLibGerichtStudent import Graph

class ProjectPlanning:
    def __init__(self):
        self.graph = Graph()
        self.activities = {}  # {activity: (duration, [predecessors])}
        self.earliest_start = {}
        self.latest_start = {}
        self.slack = {}

    def add_activity(self, activity, duration, predecessors=None):
        if predecessors is None:
            predecessors = []
        self.activities[activity] = (duration, predecessors)
        self.graph.add_vertex(activity)
        
        # Add edges from predecessors to this activity
        for pred in predecessors:
            self.graph.add_edge((pred, activity))

    def calculate_earliest_start(self):
        # Get topological sort using DFT
        # Find activities with no predecessors for starting points
        start_activities = [act for act, (_, preds) in self.activities.items() if not preds]
        
        # Initialize earliest start times
        self.earliest_start = {act: 0 for act in self.activities}
        
        # Process activities in topological order
        for activity in self.graph.DFT(start_activities[0]):
            duration = self.activities[activity][0]
            predecessors = self.activities[activity][1]
            
            if predecessors:
                self.earliest_start[activity] = max(
                    self.earliest_start[pred] + self.activities[pred][0] 
                    for pred in predecessors
                )

    def calculate_latest_start(self):
        # Initialize with a large number
        self.latest_start = {act: float('inf') for act in self.activities}
        
        # Find project end time
        project_end = max(
            self.earliest_start[act] + self.activities[act][0]
            for act in self.activities
        )
        
        # Find end activities (those that aren't predecessors to any other activity)
        end_activities = []
        for act in self.activities:
            is_end = True
            for _, preds in self.activities.values():
                if act in preds:
                    is_end = False
                    break
            if is_end:
                end_activities.append(act)
                self.latest_start[act] = project_end - self.activities[act][0]
        
        # Process activities in reverse topological order
        activities_list = self.graph.DFT(list(self.activities.keys())[0])
        for activity in reversed(activities_list):
            duration = self.activities[activity][0]
            # Find all activities that have this activity as predecessor
            successors = []
            for act, (_, preds) in self.activities.items():
                if activity in preds:
                    successors.append(act)
            
            if successors:
                self.latest_start[activity] = min(
                    self.latest_start[succ] for succ in successors
                ) - duration

    def find_critical_path(self):
        self.calculate_earliest_start()
        self.calculate_latest_start()
        
        # Calculate slack for each activity
        self.slack = {
            act: self.latest_start[act] - self.earliest_start[act]
            for act in self.activities
        }
        
        # Critical path activities have zero slack
        critical_activities = [act for act, slack in self.slack.items() if slack == 0]
        
        return critical_activities

def main():
    # Create project planning
    project = ProjectPlanning()
    
    # Add activities from the table
    project.add_activity('A', 6, [])
    project.add_activity('B', 8, [])
    project.add_activity('C', 4, ['A'])
    project.add_activity('D', 6, ['A'])
    project.add_activity('E', 3, ['B', 'C'])
    project.add_activity('F', 4, ['D'])
    project.add_activity('G', 6, ['E', 'F'])
    project.add_activity('H', 10, ['B'])
    project.add_activity('I', 2, ['H', 'G'])
    
    # Find and print critical path
    critical_path = project.find_critical_path()
    print("Kritieke pad:", ' -> '.join(critical_path))
    
    # Print additional information
    print("\nDetails per activiteit:")
    for activity in project.activities:
        print(f"Activiteit {activity}:")
        print(f"  Vroegste start: {project.earliest_start[activity]}")
        print(f"  Latest start: {project.latest_start[activity]}")
        print(f"  Slack: {project.slack[activity]}")

if __name__ == "__main__":
    main()
