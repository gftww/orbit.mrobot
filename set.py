# /home/zj-user/Ibackup/orbit/source/extensions/omni.isaac.orbit_tasks/omni/isaac/orbit_tasks/utils/wrappers/rsl_rl/vecenv_wrapper.py
    def set_commands(self, name:str, env_ids: list, vels:list):
        """Returns the current commands of the robot."""
        self.unwrapped.command_manager.set_command(name=name, env_ids=env_ids, vels=vels)
# /home/zj-user/Ibackup/orbit/source/extensions/omni.isaac.orbit/omni/isaac/orbit/managers/command_manager.py
    def set_command(self, name:str, env_ids:list, vels:list):
        return self._terms[name].set_command(env_ids, vels)
# /home/zj-user/Ibackup/orbit/source/extensions/omni.isaac.orbit/omni/isaac/orbit/envs/mdp/commands/velocity_command.py
    #UniformVelocityCommand
    def set_command(self, env_ids:list, vels:list):

        # update the metrics based on current state
        self._update_metrics()
        r = torch.tensor(vels, device=self.device)
        self.vel_command_b[env_ids,:] = r[env_ids,:]

# /home/zj-user/Ibackup/orbit/source/extensions/omni.isaac.orbit/omni/isaac/orbit/envs/rl_task_env.py
  # self.command_manager.compute(dt=self.step_dt)