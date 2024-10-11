
"use strict";

let DebugValue = require('./DebugValue.js');
let GPSINPUT = require('./GPSINPUT.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let Trajectory = require('./Trajectory.js');
let HilGPS = require('./HilGPS.js');
let RadioStatus = require('./RadioStatus.js');
let ESCStatus = require('./ESCStatus.js');
let HomePosition = require('./HomePosition.js');
let ESCInfo = require('./ESCInfo.js');
let ManualControl = require('./ManualControl.js');
let ActuatorControl = require('./ActuatorControl.js');
let HilSensor = require('./HilSensor.js');
let CellularStatus = require('./CellularStatus.js');
let RTKBaseline = require('./RTKBaseline.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let Param = require('./Param.js');
let HilControls = require('./HilControls.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let BatteryStatus = require('./BatteryStatus.js');
let FileEntry = require('./FileEntry.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let RTCM = require('./RTCM.js');
let Mavlink = require('./Mavlink.js');
let LogData = require('./LogData.js');
let MountControl = require('./MountControl.js');
let WaypointList = require('./WaypointList.js');
let Vibration = require('./Vibration.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let WaypointReached = require('./WaypointReached.js');
let CommandCode = require('./CommandCode.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let GPSRTK = require('./GPSRTK.js');
let LogEntry = require('./LogEntry.js');
let LandingTarget = require('./LandingTarget.js');
let RCIn = require('./RCIn.js');
let ParamValue = require('./ParamValue.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let VFR_HUD = require('./VFR_HUD.js');
let Waypoint = require('./Waypoint.js');
let RCOut = require('./RCOut.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let GPSRAW = require('./GPSRAW.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let ExtendedState = require('./ExtendedState.js');
let State = require('./State.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let VehicleInfo = require('./VehicleInfo.js');
let Tunnel = require('./Tunnel.js');
let SysStatus = require('./SysStatus.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let Altitude = require('./Altitude.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let Thrust = require('./Thrust.js');
let StatusText = require('./StatusText.js');
let PositionTarget = require('./PositionTarget.js');
let TerrainReport = require('./TerrainReport.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let ESCTelemetry = require('./ESCTelemetry.js');

module.exports = {
  DebugValue: DebugValue,
  GPSINPUT: GPSINPUT,
  MagnetometerReporter: MagnetometerReporter,
  Trajectory: Trajectory,
  HilGPS: HilGPS,
  RadioStatus: RadioStatus,
  ESCStatus: ESCStatus,
  HomePosition: HomePosition,
  ESCInfo: ESCInfo,
  ManualControl: ManualControl,
  ActuatorControl: ActuatorControl,
  HilSensor: HilSensor,
  CellularStatus: CellularStatus,
  RTKBaseline: RTKBaseline,
  CameraImageCaptured: CameraImageCaptured,
  Param: Param,
  HilControls: HilControls,
  PlayTuneV2: PlayTuneV2,
  HilActuatorControls: HilActuatorControls,
  BatteryStatus: BatteryStatus,
  FileEntry: FileEntry,
  TimesyncStatus: TimesyncStatus,
  RTCM: RTCM,
  Mavlink: Mavlink,
  LogData: LogData,
  MountControl: MountControl,
  WaypointList: WaypointList,
  Vibration: Vibration,
  HilStateQuaternion: HilStateQuaternion,
  AttitudeTarget: AttitudeTarget,
  WaypointReached: WaypointReached,
  CommandCode: CommandCode,
  GlobalPositionTarget: GlobalPositionTarget,
  GPSRTK: GPSRTK,
  LogEntry: LogEntry,
  LandingTarget: LandingTarget,
  RCIn: RCIn,
  ParamValue: ParamValue,
  WheelOdomStamped: WheelOdomStamped,
  VFR_HUD: VFR_HUD,
  Waypoint: Waypoint,
  RCOut: RCOut,
  ESCTelemetryItem: ESCTelemetryItem,
  GPSRAW: GPSRAW,
  CamIMUStamp: CamIMUStamp,
  ESCStatusItem: ESCStatusItem,
  EstimatorStatus: EstimatorStatus,
  ExtendedState: ExtendedState,
  State: State,
  OpticalFlowRad: OpticalFlowRad,
  OverrideRCIn: OverrideRCIn,
  VehicleInfo: VehicleInfo,
  Tunnel: Tunnel,
  SysStatus: SysStatus,
  NavControllerOutput: NavControllerOutput,
  Altitude: Altitude,
  CompanionProcessStatus: CompanionProcessStatus,
  Thrust: Thrust,
  StatusText: StatusText,
  PositionTarget: PositionTarget,
  TerrainReport: TerrainReport,
  OnboardComputerStatus: OnboardComputerStatus,
  ESCInfoItem: ESCInfoItem,
  ADSBVehicle: ADSBVehicle,
  ESCTelemetry: ESCTelemetry,
};
