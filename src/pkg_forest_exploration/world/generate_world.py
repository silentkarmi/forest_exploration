#!/usr/bin/env python3

# Author kmishra

import os
from enum import Enum

class TREE_TYPE(Enum):
  PineTree = "pine_tree"
  OakTree = "oak_tree"

WORLD_CONTENT = ""
COUNTER = 0

def pose_to_str(pose):
  str_pose = ""
  for elem in pose:
    str_pose = str_pose + str(elem) + " "

  return str_pose

def create_ground():
  global WORLD_CONTENT
  WORLD_CONTENT = WORLD_CONTENT + """<sdf version='1.6'>
  <world name='default'>
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose frame=''>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.1 0.1 0.1 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.5 -1</direction>
    </light>
    <model name='ground_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <contact>
              <ode/>
            </contact>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
    </model>
    <gravity>0 0 -9.8</gravity>
    <magnetic_field>6e-06 2.3e-05 -4.2e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
    <physics name='default_physics' default='0' type='ode'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
    <model name='mud_box'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>-6.13192 4.89997 0 0 -0 0</pose>
    </model>
    <model name='mud_box_0'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>1.90734 4.83104 0 0 -0 0</pose>
    </model>
    <model name='mud_box_1'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>-6.12792 -5.13998 0 0 -0 0</pose>
    </model>
    <model name='mud_box_2'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>1.85975 -5.14192 0 0 -0 0</pose>
    </model>
    <state world_name='default'>
      <sim_time>2682 546000000</sim_time>
      <real_time>1154 674258672</real_time>
      <wall_time>1552470976 109554706</wall_time>
      <iterations>1149829</iterations>
      <model name='ground_plane'>
        <pose frame=''>0 0 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>0 0 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box'>
        <pose frame=''>9.86832 14.8407 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>9.86832 14.8407 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_0'>
        <pose frame=''>1.86767 4.83104 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>1.86767 4.83104 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_0_clone'>
        <pose frame=''>9.85757 -5.14216 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>9.85757 -5.14216 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_0_clone_clone'>
        <pose frame=''>17.8643 -5.17973 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>17.8643 -5.17973 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_0_clone_clone_0'>
        <pose frame=''>17.8432 4.79546 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>17.8432 4.79546 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_0_clone_clone_1'>
        <pose frame=''>25.8322 4.79818 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>25.8322 4.79818 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_0_clone_clone_2'>
        <pose frame=''>1.86503 14.8262 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>1.86503 14.8262 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_1'>
        <pose frame=''>25.8304 -5.18145 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>25.8304 -5.18145 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_2'>
        <pose frame=''>1.85975 -5.14192 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>1.85975 -5.14192 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_3'>
        <pose frame=''>17.8698 14.7961 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>17.8698 14.7961 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_4'>
        <pose frame=''>9.86465 4.85433 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>9.86465 4.85433 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='mud_box_5'>
        <pose frame=''>25.863 14.7854 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose frame=''>25.863 14.7854 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <light name='sun'>
        <pose frame=''>0 0 10 0 -0 0</pose>
      </light>
    </state>
    <gui fullscreen='0'>
      <camera name='user_camera'>
        <pose frame=''>-24.2352 -31.8678 23.6446 0 0.457797 0.789301</pose>
        <view_controller>orbit</view_controller>
        <projection_type>perspective</projection_type>
      </camera>
    </gui>
    <model name='mud_box_0_clone'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>9.81681 -5.15165 0 0 -0 0</pose>
    </model>
    <model name='mud_box_0_clone_clone'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>17.8709 -5.12525 0 0 -0 0</pose>
    </model>
    <model name='mud_box_0_clone_clone_0'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>17.8432 4.79546 0 0 -0 0</pose>
    </model>
    <model name='mud_box_0_clone_clone_1'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>-14.1276 -5.15209 0 0 -0 0</pose>
    </model>
    <model name='mud_box_0_clone_clone_2'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>-14.0968 4.86277 0 0 -0 0</pose>
    </model> 
    <model name='mud_box_4'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>9.86465 4.85433 0 0 -0 0</pose>
    </model>
    <model name='mud_box_3'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>18.293 14.7207 0 0 -0 0</pose>
    </model>
    <model name='mud_box_5'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <box>
              <size>8 10 0.2</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='visual_1'>
          <pose frame=''>-2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_2'>
          <pose frame=''>2 2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_3'>
          <pose frame=''>2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <visual name='visual_4'>
          <pose frame=''>-2 -2.5 0 0 -0 0</pose>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <box>
              <size>4 5 0.2</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>model://mud_box/materials/scripts</uri>
              <uri>model://mud_box/materials/textures</uri>
              <name>vrc/mud</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>26.0626 14.6614 0 0 -0 0</pose>
    </model>"""
  
def add_tree(tree_type, pose):
  add_tree.counter += 1
  print(tree_type.value)
  str_pose = pose_to_str(pose)

  print(str_pose)

  global WORLD_CONTENT
  WORLD_CONTENT = WORLD_CONTENT + """<model name='""" + tree_type.value + str(add_tree.counter) +"""'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <mesh>
              <uri>model://""" + tree_type.value +"""/meshes/""" + tree_type.value +""".dae</uri>
              <scale>1 1 1</scale>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <visual name='branch'>
          <geometry>
            <mesh>
              <uri>model://""" + tree_type.value +"""/meshes/""" + tree_type.value +""".dae</uri>
              <submesh>
                <name>Branch</name>
              </submesh>
              <scale>1 1 1</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>model://""" + tree_type.value +"""/materials/scripts/</uri>
              <uri>model://""" + tree_type.value +"""/materials/textures/</uri>
              <name>""" + tree_type.name +"""/Branch</name>
            </script>
          </material>
        </visual>
        <visual name='bark'>
          <geometry>
            <mesh>
              <uri>model://""" + tree_type.value +"""/meshes/""" + tree_type.value +""".dae</uri>
              <submesh>
                <name>Bark</name>
              </submesh>
              <scale>1 1 1</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>model://""" + tree_type.value +"""/materials/scripts/</uri>
              <uri>model://""" + tree_type.value +"""/materials/textures/</uri>
              <name>""" + tree_type.name +"""/Bark</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <pose frame=''>""" + pose_to_str(pose) + """</pose>
    </model>"""
  
def finish_ground():
  global WORLD_CONTENT
  WORLD_CONTENT = WORLD_CONTENT + """ </world>
</sdf>"""  

def main():
  global WORLD_CONTENT
  os.chdir(os.path.dirname(__file__))
  print(os.getcwd())

  create_ground()

  add_tree.counter  = 0
  add_tree(TREE_TYPE.OakTree, (19.9234, 7.95912, 0, 0, -0, 0))
  add_tree(TREE_TYPE.PineTree, (0, 0, 0, 0, -0, 0))
  add_tree(TREE_TYPE.PineTree, (5, 5, 0, 0, -0, 0))
  add_tree(TREE_TYPE.OakTree, (10, 10, 0, 0, -0, 0))
  add_tree(TREE_TYPE.PineTree, (15, 15, 0, 0, -0, 0))

  finish_ground()

  f = open("generated_world.world", "w")
  f.write(WORLD_CONTENT)
  f.close()

if __name__=="__main__":
  main()
