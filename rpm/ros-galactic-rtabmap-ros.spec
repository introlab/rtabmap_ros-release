%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-rtabmap-ros
Version:        0.20.16
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rtabmap_ros package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-builtin-interfaces
Requires:       ros-galactic-class-loader
Requires:       ros-galactic-compressed-depth-image-transport
Requires:       ros-galactic-compressed-image-transport
Requires:       ros-galactic-cv-bridge
Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-image-geometry
Requires:       ros-galactic-image-transport
Requires:       ros-galactic-laser-geometry
Requires:       ros-galactic-message-filters
Requires:       ros-galactic-nav-msgs
Requires:       ros-galactic-nav2-common
Requires:       ros-galactic-octomap
Requires:       ros-galactic-octomap-msgs
Requires:       ros-galactic-pcl-conversions
Requires:       ros-galactic-pluginlib
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-rclcpp-components
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-rosgraph-msgs
Requires:       ros-galactic-rosidl-default-runtime
Requires:       ros-galactic-rtabmap
Requires:       ros-galactic-rviz-common
Requires:       ros-galactic-rviz-default-plugins
Requires:       ros-galactic-rviz-rendering
Requires:       ros-galactic-sensor-msgs
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-std-srvs
Requires:       ros-galactic-stereo-msgs
Requires:       ros-galactic-tf2
Requires:       ros-galactic-tf2-eigen
Requires:       ros-galactic-tf2-ros
Requires:       ros-galactic-visualization-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  pcl-devel
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-builtin-interfaces
BuildRequires:  ros-galactic-class-loader
BuildRequires:  ros-galactic-cv-bridge
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-image-geometry
BuildRequires:  ros-galactic-image-transport
BuildRequires:  ros-galactic-laser-geometry
BuildRequires:  ros-galactic-message-filters
BuildRequires:  ros-galactic-nav-msgs
BuildRequires:  ros-galactic-octomap
BuildRequires:  ros-galactic-octomap-msgs
BuildRequires:  ros-galactic-pcl-conversions
BuildRequires:  ros-galactic-pluginlib
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-rclcpp-components
BuildRequires:  ros-galactic-rclpy
BuildRequires:  ros-galactic-rosgraph-msgs
BuildRequires:  ros-galactic-rosidl-default-generators
BuildRequires:  ros-galactic-rtabmap
BuildRequires:  ros-galactic-rviz-common
BuildRequires:  ros-galactic-rviz-default-plugins
BuildRequires:  ros-galactic-rviz-rendering
BuildRequires:  ros-galactic-sensor-msgs
BuildRequires:  ros-galactic-std-msgs
BuildRequires:  ros-galactic-std-srvs
BuildRequires:  ros-galactic-stereo-msgs
BuildRequires:  ros-galactic-tf2
BuildRequires:  ros-galactic-tf2-eigen
BuildRequires:  ros-galactic-tf2-ros
BuildRequires:  ros-galactic-visualization-msgs
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-galactic-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-galactic-rosidl-interface-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-galactic-rosidl-interface-packages(all)
%endif

%description
RTAB-Map's ros-pkg. RTAB-Map is a RGB-D SLAM approach with real-time
constraints.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Sun Dec 26 2021 Mathieu Labbe <matlabbe@gmail.com> - 0.20.16-1
- Autogenerated by Bloom

* Fri Nov 12 2021 Mathieu Labbe <matlabbe@gmail.com> - 0.20.15-2
- Autogenerated by Bloom

* Mon Nov 08 2021 Mathieu Labbe <matlabbe@gmail.com> - 0.20.15-1
- Autogenerated by Bloom

