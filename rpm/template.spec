Name:           ros-jade-rtabmap-ros
Version:        0.11.7
Release:        0%{?dist}
Summary:        ROS rtabmap_ros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-class-loader
Requires:       ros-jade-costmap-2d
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-eigen-conversions
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-transport
Requires:       ros-jade-image-transport-plugins
Requires:       ros-jade-laser-geometry
Requires:       ros-jade-message-filters
Requires:       ros-jade-move-base-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-nodelet
Requires:       ros-jade-octomap
Requires:       ros-jade-octomap-ros
Requires:       ros-jade-pcl-conversions
Requires:       ros-jade-pcl-ros
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-rtabmap
Requires:       ros-jade-rviz
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-stereo-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
Requires:       ros-jade-tf2-ros
Requires:       ros-jade-visualization-msgs
BuildRequires:  pcl-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-class-loader
BuildRequires:  ros-jade-costmap-2d
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-eigen-conversions
BuildRequires:  ros-jade-genmsg
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-laser-geometry
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-move-base-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-octomap
BuildRequires:  ros-jade-octomap-ros
BuildRequires:  ros-jade-pcl-conversions
BuildRequires:  ros-jade-pcl-ros
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rtabmap
BuildRequires:  ros-jade-rviz
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-stereo-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions
BuildRequires:  ros-jade-tf2-ros
BuildRequires:  ros-jade-visualization-msgs

%description
RTAB-Map's ros-pkg. RTAB-Map is a RGB-D SLAM approach with real-time
constraints.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Jun 01 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.11.7-0
- Autogenerated by Bloom

* Sat May 14 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.11.5-0
- Autogenerated by Bloom

* Thu Mar 24 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-1
- Autogenerated by Bloom

* Sat Oct 17 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.10.4-0
- Autogenerated by Bloom

* Thu May 14 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.9.0-0
- Autogenerated by Bloom

* Tue May 12 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.12-1
- Autogenerated by Bloom

