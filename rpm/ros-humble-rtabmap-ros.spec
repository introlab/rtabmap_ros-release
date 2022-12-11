%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rtabmap-ros
Version:        0.20.22
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rtabmap_ros package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-builtin-interfaces
Requires:       ros-humble-class-loader
Requires:       ros-humble-compressed-depth-image-transport
Requires:       ros-humble-compressed-image-transport
Requires:       ros-humble-cv-bridge
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-image-geometry
Requires:       ros-humble-image-transport
Requires:       ros-humble-laser-geometry
Requires:       ros-humble-message-filters
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-nav2-common
Requires:       ros-humble-nav2-msgs
Requires:       ros-humble-octomap
Requires:       ros-humble-octomap-msgs
Requires:       ros-humble-pcl-conversions
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-components
Requires:       ros-humble-rclpy
Requires:       ros-humble-rosgraph-msgs
Requires:       ros-humble-rosidl-default-runtime
Requires:       ros-humble-rtabmap
Requires:       ros-humble-rviz-common
Requires:       ros-humble-rviz-default-plugins
Requires:       ros-humble-rviz-rendering
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-std-srvs
Requires:       ros-humble-stereo-msgs
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-eigen
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-visualization-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  pcl-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-cmake-python
BuildRequires:  ros-humble-builtin-interfaces
BuildRequires:  ros-humble-class-loader
BuildRequires:  ros-humble-cv-bridge
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-image-geometry
BuildRequires:  ros-humble-image-transport
BuildRequires:  ros-humble-laser-geometry
BuildRequires:  ros-humble-message-filters
BuildRequires:  ros-humble-nav-msgs
BuildRequires:  ros-humble-nav2-msgs
BuildRequires:  ros-humble-octomap
BuildRequires:  ros-humble-octomap-msgs
BuildRequires:  ros-humble-pcl-conversions
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-components
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-ros-environment
BuildRequires:  ros-humble-rosgraph-msgs
BuildRequires:  ros-humble-rosidl-default-generators
BuildRequires:  ros-humble-rtabmap
BuildRequires:  ros-humble-rviz-common
BuildRequires:  ros-humble-rviz-default-plugins
BuildRequires:  ros-humble-rviz-rendering
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-std-srvs
BuildRequires:  ros-humble-stereo-msgs
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-eigen
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-visualization-msgs
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-humble-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-humble-rosidl-interface-packages(all)
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Sun Dec 11 2022 Mathieu Labbe <matlabbe@gmail.com> - 0.20.22-1
- Autogenerated by Bloom

* Mon Oct 03 2022 Mathieu Labbe <matlabbe@gmail.com> - 0.20.20-2
- Autogenerated by Bloom

* Sat Oct 01 2022 Mathieu Labbe <matlabbe@gmail.com> - 0.20.20-1
- Autogenerated by Bloom

