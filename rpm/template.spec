%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rtabmap-msgs
Version:        0.21.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rtabmap_msgs package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-rosidl-default-runtime
Requires:       ros-iron-sensor-msgs
Requires:       ros-iron-std-msgs
Requires:       ros-iron-std-srvs
Requires:       ros-iron-ros-workspace
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-rosidl-default-generators
BuildRequires:  ros-iron-sensor-msgs
BuildRequires:  ros-iron-std-msgs
BuildRequires:  ros-iron-std-srvs
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-iron-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-iron-rosidl-interface-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-iron-rosidl-interface-packages(all)
%endif

%description
RTAB-Map's msgs package.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
    -DCATKIN_ENABLE_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%files
/opt/ros/iron

%changelog
* Thu Jan 04 2024 Mathieu Labbe <matlabbe@gmail.com> - 0.21.3-1
- Autogenerated by Bloom

* Sat Aug 05 2023 Mathieu Labbe <matlabbe@gmail.com> - 0.21.2-1
- Autogenerated by Bloom

