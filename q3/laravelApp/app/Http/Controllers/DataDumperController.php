<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class DataDumperController extends Controller
{
    public function getData(){
        $data = DB::table('device')->join('report', 'device.ID', '=', 'report.Device_ID')->get();
        return $data;
    }
}
